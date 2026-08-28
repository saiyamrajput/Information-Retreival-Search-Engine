## Day 6:

Query:
"what similarity laws must be obeyed when constructing aeroelastic models of heated high speed aircraft."

## TF-IDF Top 10
13, 51, 12, 486, 184, 327, 746, 1268, 878, 665

## BM25 Top 10
13, 486, 12, 878, 184, 51, 1144, 746, 914, 747

## Finding:

BM25 produced a different ranking from TF-IDF for the same Cranfield query. Both methods ranked Document 13 first, but several of the remaining documents changed positions. For example, Document 486 moved from 4th place with TF-IDF to 2nd place with BM25, while Document 51 moved from 2nd place to 6th place. This shows that BM25 ranks documents differently because it considers term-frequency saturation and document-length normalization rather than relying only on the TF-IDF cosine similarity. Seven documents were common between the two Top 10 lists, but their ordering was different. The BM25 top-ranked documents were also semantically relevant to the query. However, these results alone do not show that BM25 is better than TF-IDF.