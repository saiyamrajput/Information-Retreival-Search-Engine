import sys
sys.path.append("src")

from ranking import inverse_document_frequency, document_frequency, term_frequency, tf_idf, document_vector, query_vector, cosine_similarity, rank_retrieval, document_length, average_document_length, bm25_idf, bm25_term_score, bm25_document_score, bm25_rank_retrieval
from preprocessing import tokenizer, load, inverted_index

inverted_index1 = {
    "wing": {1: 2, 2: 1},
    "flow": {1: 1},
    "pressure": {2: 1, 3: 1}
}

N = 3

query = "The effects of wing pressure and air flow on aircraft performance."

terms = tokenizer(query)

for t in terms:
    print("Term:", t)
    print("DF:", document_frequency(t, inverted_index1))
    print("IDF:", inverse_document_frequency(t, inverted_index1, N))
    print()

# checking term frequency
print('TF("wing", 1):', term_frequency("wing", inverted_index1, 1))
print('TF("wing", 2):', term_frequency("wing", inverted_index1, 2))
print('TF("wing", 3):', term_frequency("wing",inverted_index1, 3))
print('\nTF("flow", 1):', term_frequency("flow", inverted_index1, 1))
print('TF("flow", 2):', term_frequency("flow", inverted_index1, 2))
print('\nTF("computer", 1):', term_frequency("computer", inverted_index1, 1))

# checking tf-idf
print('\nTF-IDF("wing", D1):', tf_idf("wing", 1, inverted_index1, N))
print('TF-IDF("wing", D2):', tf_idf("wing", 2, inverted_index1, N))
print('\nTF-IDF("flow", D1):', tf_idf("flow", 1, inverted_index1, N))
print('\nTF-IDF("pressure", D3):', tf_idf("pressure", 3, inverted_index1, N))
print('\nTF-IDF("computer", D1):', tf_idf("computer", 1, inverted_index1, N))

# document vectors
vocabulary = list(inverted_index1.keys())
print("\nD1:", document_vector(1, inverted_index1, N, vocabulary))
print("D2:", document_vector(2, inverted_index1, N, vocabulary))
print("D3:", document_vector(3, inverted_index1, N, vocabulary))

# query vector
print("\nQuery:", query)
print("\nQuery terms:", terms)
print("\nQuery vector:", query_vector(query, inverted_index1, N, vocabulary))

# cosine similarity
q_vector = query_vector(query, inverted_index1, N, vocabulary)

d1_vector = document_vector(1, inverted_index1, N, vocabulary)
d2_vector = document_vector(2, inverted_index1, N, vocabulary)
d3_vector = document_vector(3, inverted_index1, N, vocabulary)

print("Query vs D1:", cosine_similarity(q_vector, d1_vector))
print("Query vs D2:", cosine_similarity(q_vector, d2_vector))
print("Query vs D3:", cosine_similarity(q_vector, d3_vector))

# rank retrieval
documentIDs = [1, 2, 3]

print(rank_retrieval(query, inverted_index1, N, vocabulary, documentIDs))


# Cranfield Corpus Testing

documents_cranfield = load("../cran/cran.all.1400")

invertedIndex_cranfield = inverted_index(documents_cranfield)

N_cranfield = len(documents_cranfield)

vocabulary = list(invertedIndex_cranfield.keys())

documentIDs = [document["Document ID"] for document in documents_cranfield]

query_cranfield = "what similarity laws must be obeyed when constructing aeroelastic models of heated high speed aircraft."

finalResult = rank_retrieval(query_cranfield, invertedIndex_cranfield, N_cranfield, vocabulary, documentIDs)

print("\nQuery:", query_cranfield)
print("\nTotal Documents (N):", N_cranfield)
print("\nVocabulary:", len(vocabulary))

print("\nTop 10 results:")
print(finalResult[:10])

# confirming top 3 is correct or not
top3 = finalResult[:3]

print("\nTop 3 Document Details:")

for i, j in top3:
    for k in documents_cranfield:
        if k["Document ID"] == i:
            print("\nDocument ID:", k["Document ID"])
            print("Similarity Score:", j)
            print("Title:", k["Title"])
            print("Text:", k["Text"][:300])
            break

# checking document length and average document length on cranfield corpus
for document in documents_cranfield[: 3]:
    print("Document:", document["Document ID"])
    print("Length:", document_length(document))
    print()

print("Average document length:", average_document_length(documents_cranfield))

# checking documetn length and averge length using tiny example
tiny_documents = [
    {"Document ID": 1, "Text": "wing flow wing"},
    {"Document ID": 2, "Text": "pressure wing"},
    {"Document ID": 3, "Text": "aircraft pressure flow wing"}
]

print("Tiny document lengths:")

for document in tiny_documents:
    print("Document:", document["Document ID"], "\nLength:", document_length(document))
    print()

print("Average:", average_document_length(tiny_documents))

# checking bm25_idf
print("\nBM25 IDF:")

print("wing:", bm25_idf("wing", inverted_index1, N))
print("flow:", bm25_idf("flow", inverted_index1, N))
print("pressure:", bm25_idf("pressure", inverted_index1, N))

# checking bm25 term function
print("\nBM25 term score:")
tiny_document_length = document_length(tiny_documents[0])
tiny_document_length_average = average_document_length(tiny_documents)

score_term = bm25_term_score("wing", 1, inverted_index1, N, tiny_document_length, tiny_document_length_average)

print('BM25("wing", D1):', score_term)

# checking bm25 document function
score_document = bm25_document_score(query,tiny_documents[0], inverted_index1, N, tiny_document_length_average)

print("\nBM25(", query, "D1)", score_document)

# checking bm25 rank retrieval
tiny_index = inverted_index(tiny_documents)
N_tiny = len(tiny_documents)

query_tiny = "wing flow"

tiny_BM25 = bm25_rank_retrieval(query_tiny, tiny_documents, tiny_index, N_tiny)

print(tiny_BM25)

# checking BM25 on cranfield corpus
finalResult_BM25 = bm25_rank_retrieval(query_cranfield, documents_cranfield, invertedIndex_cranfield, N_cranfield)

print("\nTF-IDF Top 10:")
print(finalResult[:10])

print("\nBM25 Top 10:")
print(finalResult_BM25[:10])

print("\nBM25 Top 3 Document Details:")

for i, j in finalResult_BM25[:3]:
    for k in documents_cranfield:
        if k["Document ID"] == i:
            print("\nDocument ID:", k["Document ID"])
            print("BM25 Score:", j)
            print("Title:", k["Title"])
            print("Text:", k["Text"][:300])
            break
