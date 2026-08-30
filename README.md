# Information Retrieval Search Engine

## Project Overview

This project implements an information retrieval search engine using the Cranfield collection. I began with basic Boolean retrieval and then extended the system to ranked retrieval so that documents could be ordered by their estimated relevance to a query. For ranked retrieval, I implemented TF-IDF with cosine similarity and BM25, and compared example rankings produced by the two methods. The system also supports retrieval evaluation using Cranfield relevance judgments with Precision@K and Recall@K.

## Corpus

The project uses the Cranfield collection as its benchmark corpus. It contains:

* **Documents:** 1,400
* **Queries:** 225
* **Relevance judgments:** Available for evaluating retrieved results

The project uses three main Cranfield files:

* `cran.all.1400` - document collection
* `cran.qry` - benchmark queries
* `cranqrel` - relevance judgments

The relevance judgments specify which documents are considered relevant to each benchmark query. This makes it possible to evaluate retrieval quality quantitatively rather than relying only on manual inspection of search results.

## Architecture

The search engine is divided into four main Python modules. Each module handles a different stage of the retrieval pipeline, from loading and preprocessing the Cranfield data to retrieving, ranking, and evaluating documents.

```text
                    Cranfield Collection
                            |
          -----------------------------------------
          |                    |                  |
   cran.all.1400           cran.qry           cranqrel
     documents              queries             qrels
          |                    |                  |
          ---------------------|------------------
                            |
                     preprocessing.py
                            |
          --------------------------------
          |              |               |
      Tokenizer      Query Loading    Qrels Loading
          |
     Inverted Index
          |
      -------------------------
      |                       |
 retrieval.py             ranking.py
      |                       |
Boolean Retrieval       Ranked Retrieval
                         |            |
                TF-IDF + Cosine     BM25
                    Similarity        |
                        |             |
                        |             |
                       Ranked Documents
                              |
                        evaluation.py
                              |
                   Precision@K / Recall@K
```

### `preprocessing.py`

This module handles data loading and text preprocessing for the Cranfield collection. It loads the documents from `cran.all.1400`, the benchmark queries from `cran.qry`, and the relevance judgments from `cranqrel`. It also tokenizes text by converting it to lowercase, removing punctuation and stop words, and builds the inverted index used by the retrieval and ranking methods.

### `retrieval.py`

This module handles basic Boolean retrieval using the inverted index. It supports single-term retrieval and multiple-term retrieval using AND and OR operations. Queries are tokenized before the selected retrieval operation is performed.

### `ranking.py`

This module handles ranked retrieval. It contains the term-frequency and inverse-document-frequency calculations used to construct TF-IDF document and query vectors, along with cosine similarity for ranking documents. It also contains the BM25 implementation, including document-length calculation, average document length, BM25 IDF, term scoring, document scoring, and ranked BM25 retrieval.

### `evaluation.py`

This module handles retrieval evaluation. It implements Precision@K and Recall@K, which compare the top-ranked retrieved documents with the known relevant documents for each Cranfield query.

## Retrieval Methods

The search engine supports three main retrieval and ranking approaches: Boolean retrieval, TF-IDF with cosine similarity, and BM25.

### Boolean Retrieval

Boolean retrieval uses the inverted index to find documents containing the terms in a query. The system supports single-term retrieval as well as `AND` and `OR` operations.

* **Single-term retrieval** returns documents containing a specific term.
* **AND retrieval** returns documents containing all query terms.
* **OR retrieval** returns documents containing at least one query term.

Queries are tokenized before retrieval so that the same preprocessing steps are applied to both the queries and the document collection.

### TF-IDF and Cosine Similarity

For ranked retrieval, the search engine uses TF-IDF to assign weights to terms. Term frequency measures how often a term occurs in a document, while inverse document frequency gives less weight to terms that occur in many documents across the collection.

The system creates TF-IDF vectors for documents and queries and uses cosine similarity to measure their similarity. Documents are then ranked by cosine similarity, with the highest-scoring documents returned first.

### BM25

BM25 provides an alternative ranked retrieval method. It considers term frequency, inverse document frequency, document length, and average document length when calculating a document's relevance score.

Unlike basic TF-IDF weighting, BM25 includes term-frequency saturation, meaning that repeated occurrences of a query term continue to increase a document's score but with diminishing impact. It also normalizes scores based on document length so that longer documents are not automatically favored simply because they contain more terms.

The implementation uses `k = 1.5` and `b = 0.75`. Each document receives a BM25 score for a query, and the documents are ranked from highest to lowest score.

## Evaluation and Current Results

The retrieval system is evaluated using Precision@K and Recall@K. Precision@K measures the proportion of the top K retrieved documents that are relevant, while Recall@K measures the proportion of all relevant documents that appear within the top K retrieved results.

For the current Cranfield evaluation, I used the relevance judgments from `cranqrel` and evaluated the first four query records from `cran.qry`. These records have Query IDs 1, 2, 4, and 8.

| Query ID | Precision@10 | Recall@10 |
| -------: | -----------: | --------: |
|        1 |         0.40 |    0.1429 |
|        2 |         0.40 |    0.1667 |
|        4 |         0.00 |    0.0000 |
|        8 |         0.00 |    0.0000 |

These results represent only four Cranfield queries and should not be interpreted as an overall measurement of retrieval performance. No average Precision@10 or Recall@10 is reported because the complete set of 225 Cranfield queries has not yet been evaluated.

### TF-IDF vs BM25

Both TF-IDF with cosine similarity and BM25 are implemented in the search engine. I compared their rankings for an example Cranfield query to examine how the two methods order the same document collection.

Both methods ranked Document 13 first, but several other documents changed positions. For example, Document 486 moved from fourth place with TF-IDF to second place with BM25, while Document 51 moved from second place with TF-IDF to sixth place with BM25. Seven documents were shared between the two Top 10 result sets, although their ordering differed.

**Top 10 Documents Retrieved by Both Methods**

| TF-IDF   | BM25   |
| -------: | -----: |
|       13 |     13 |
|       51 |    486 |
|       12 |     12 |
|      486 |    878 |
|      184 |    184 |
|      327 |     51 |
|      746 |   1144 |
|     1268 |    746 |
|      878 |    914 |
|      665 |    747 |

This comparison demonstrates that TF-IDF and BM25 can produce different rankings for the same query. However, it represents only an example comparison and does not show that either method performs better overall. A systematic evaluation across the Cranfield query set would be required before making a general performance claim about the two ranking methods.


## Limitations

The current evaluation uses only four Cranfield query records rather than the complete set of 225 queries. Because of this, the current Precision@10 and Recall@10 results cannot be used to describe the overall performance of the search engine.

The TF-IDF and BM25 comparison is also limited to example rankings. BM25 has not yet been systematically benchmarked against TF-IDF across the complete Cranfield query set.

The current evaluation focuses on Precision@10 and Recall@10. Additional retrieval metrics could provide a more complete view of ranking quality in future experiments.

The project also currently focuses on retrieval quality rather than system efficiency. Query latency, indexing time, and index size have not yet been measured.

## Next Experiments / Benchmarking

The next step is to evaluate the search engine using the complete set of 225 Cranfield queries. For each query, the system will retrieve and rank documents and compare the results against the corresponding relevance judgments in `cranqrel`.

Precision@10 and Recall@10 can then be calculated for each query and summarized across the query set to provide a broader view of retrieval performance.

The same evaluation procedure can be applied to both TF-IDF and BM25 so that the two ranking methods can be compared using a consistent benchmark rather than individual example queries.

Future evaluation can also include additional ranking metrics to provide a more complete assessment of retrieval quality.

Beyond retrieval effectiveness, later experiments will measure system efficiency, including query latency, indexing time, and inverted-index size. These measurements will help evaluate the tradeoff between retrieval quality and computational performance.

## Repository Structure

The repository is organized into separate modules for preprocessing, retrieval, ranking, and evaluation.

```text
Information-Retrieval-Search-Engine/
|
|-- cran/                         # local corpus directory (gitignored)
|   |-- cran.all.1400
|   |-- cran.qry
|   |-- cranqrel
|
|-- results/
|   |-- Day-6-Findings.md
|
|-- src/
|   |-- evaluation.py
|   |-- preprocessing.py
|   |-- ranking.py
|   |-- retrieval.py
|
|-- tests/
|   |-- test_evaluation.py
|   |-- test_preprocessing.py
|   |-- test_ranking.py
|   |-- test_retrieval.py
|
|-- .gitignore
|-- requirements.txt
|-- README.md
```

The `src/` directory contains the main search-engine implementation, while the `tests/` directory contains tests for preprocessing, retrieval, ranking, and evaluation.

The `cran/` directory is required locally to run the project but is excluded from the repository through `.gitignore`. It contains the Cranfield document collection, benchmark queries, and relevance judgments used by the experiments.

## How to Reproduce

1. Clone the repository.

2. Install the required Python dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `cran/` directory in the project root.

4. Obtain the Cranfield collection and place the following files inside `cran/`:

```text
cran/
|-- cran.all.1400
|-- cran.qry
|-- cranqrel
```

These corpus files are not included in this repository.

5. Run the test files in the `tests/` directory to reproduce the preprocessing, retrieval, ranking, and evaluation checks.
