### The Cranfield corpus files are not committed to this repository. Place the required Cranfield files in the local `cran/` directory before running the indexer.

## Day 1

## Document Representation

Each Cranfield document will be represented using four fields:

- `Document ID` - Unique identifier for the document
- `Title` - Title of the scientific document
- `Author` - Author of the document
- `Text` - Main searchable text of the document

## Tokenizer Design

The tokenizer will use the following interface:

`tokenize(text) -> list[str]`

The tokenizer will process text in the following order:

1. Convert all text to lowercase.
2. Remove punctuation.
3. Split the text into individual words/tokens.
4. Remove stop words using `scikit-learn`.
5. Return the resulting list of tokens.

For example:

`"The Aircraft flies quickly."`

will become:

`["aircraft", "flies", "quickly"]`

## Day 2

### Corpus
- **Cranfield collection:** 1,400 documents

### Document Format
The Cranfield documents use the following tagged format:

- `.I` - Document ID
- `.T` - Title
- `.A` - Author
- `.B` - Bibliography
- `.W` - Document text

### Document Loader
The document loader:
- Parses the Cranfield tagged document format
- Extracts the document ID, title, author, and searchable text
- Ignores the `.B` bibliography field for indexing
- Accepts a `file_path` argument rather than relying on a hard-coded path
- Successfully loads all **1,400 documents**

### Tokenizer Decisions
The tokenizer:
- Converts text to lowercase
- Removes punctuation
- Splits text into individual tokens
- Removes English stop words using `scikit-learn`
- Keeps repeated terms so that **term frequency (TF)** can be calculated

### Inverted Index

The inverted index uses the following nested-dictionary structure:

```text
{
    Word/Term: {
                    document_id: term_frequency
               }
}