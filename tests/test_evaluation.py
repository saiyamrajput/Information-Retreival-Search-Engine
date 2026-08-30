import sys
sys.path.append("src")

from evaluation import precision_at_k, recall_at_k
from ranking import rank_retrieval
from preprocessing import load, inverted_index, load_query, load_qrels


# checking precision and reacall at k under tiny corpus
rankedList_tinyCorpus = [(13, 0.9), (51, 0.8), (99, 0.7), (12, 0.6), (500, 0.5)]
relevant_documentIDs_tinyCorpus = [13, 51, 12, 184]
k_tinyCorpus = 5

precision_tinyCorpus = precision_at_k(rankedList_tinyCorpus, relevant_documentIDs_tinyCorpus, k_tinyCorpus)

assert precision_tinyCorpus == 0.6

recall_tinyCorpus = recall_at_k(rankedList_tinyCorpus, relevant_documentIDs_tinyCorpus, k_tinyCorpus)

assert recall_tinyCorpus == 0.75

# checking load_qrels and load_query
qrels = load_qrels("cran/cranqrel")
queries = load_query("cran/cran.qry")

query_by_id = {}

for query in queries:
    query_by_id[query["Query ID"]] = query["Text"]

query1 = qrels[1]

assert len(query1) == 28

assert 13 in query1
assert 51 in query1
assert 12 in query1
assert 184 in query1
assert 285 not in query1

# checking precision and recall using ranked retrieval we created in ranking.py
# Cranfield Corpus Testing

documents_cranfield = load("cran/cran.all.1400")

invertedIndex_cranfield = inverted_index(documents_cranfield)

N_cranfield = len(documents_cranfield)

vocabulary = list(invertedIndex_cranfield.keys())

documentIDs = [document["Document ID"] for document in documents_cranfield]

query_cranfield_1 = query_by_id[1]
finalResult_1 = rank_retrieval(query_cranfield_1, invertedIndex_cranfield, N_cranfield, vocabulary, documentIDs)

relevant_documentIDs_Cranfield_1 = qrels[1]
relevant_documentIDs_Cranfield_2 = qrels[2]
relevant_documentIDs_Cranfield_3 = qrels[4]
relevant_documentIDs_Cranfield_4 = qrels[8]

k_Cranfield = 10

precision_Cranfield_1 = precision_at_k(finalResult_1, relevant_documentIDs_Cranfield_1, k_Cranfield)
recall_Cranfield_1 = recall_at_k(finalResult_1, relevant_documentIDs_Cranfield_1, k_Cranfield)

assert precision_Cranfield_1 == 0.4
assert abs(recall_Cranfield_1 - (4/28)) < 0.000001

query_cranfield_2 = query_by_id[2]
finalResult_2 = rank_retrieval(query_cranfield_2, invertedIndex_cranfield, N_cranfield, vocabulary, documentIDs)

precision_Cranfield_2 = precision_at_k(finalResult_2, relevant_documentIDs_Cranfield_2, k_Cranfield)
recall_Cranfield_2 = recall_at_k(finalResult_2, relevant_documentIDs_Cranfield_2, k_Cranfield)

query_cranfield_4 = query_by_id[4]
finalResult_4 = rank_retrieval(query_cranfield_4, invertedIndex_cranfield, N_cranfield, vocabulary, documentIDs)

precision_Cranfield_4 = precision_at_k(finalResult_4, relevant_documentIDs_Cranfield_3, k_Cranfield)
recall_Cranfield_4 = recall_at_k(finalResult_4, relevant_documentIDs_Cranfield_3, k_Cranfield)

query_cranfield_8 = query_by_id[8]
finalResult_8 = rank_retrieval(query_cranfield_8, invertedIndex_cranfield, N_cranfield, vocabulary, documentIDs)

precision_Cranfield_8 = precision_at_k(finalResult_8, relevant_documentIDs_Cranfield_4, k_Cranfield)
recall_Cranfield_8 = recall_at_k(finalResult_8, relevant_documentIDs_Cranfield_4, k_Cranfield)

print("Query 1 Precision@10:", precision_Cranfield_1)
print("Query 1 Recall@10:", recall_Cranfield_1)

print("\nQuery 2 Precision@10:", precision_Cranfield_2)
print("Query 2 Recall@10:", recall_Cranfield_2)

print("\nQuery 4 Precision@10:", precision_Cranfield_4)
print("Query 4 Recall@10:", recall_Cranfield_4)

print("\nQuery 8 Precision@10:", precision_Cranfield_8)
print("Query 8 Recall@10:", recall_Cranfield_8)

comparisonTable = [
    {
        "Query": 1,
        "Precision@10": precision_Cranfield_1,
        "Recall@10": recall_Cranfield_1
    },
    {
        "Query": 2,
        "Precision@10": precision_Cranfield_2,
        "Recall@10": recall_Cranfield_2
    },
    {
        "Query": 4,
        "Precision@10": precision_Cranfield_4,
        "Recall@10": recall_Cranfield_4
    },
    {
        "Query": 8,
        "Precision@10": precision_Cranfield_8,
        "Recall@10": recall_Cranfield_8
    }
]

print("\n")

for row in comparisonTable:
    print(row)
