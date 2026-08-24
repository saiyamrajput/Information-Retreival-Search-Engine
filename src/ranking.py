import math
from preprocessing import tokenizer

def document_frequency(term, inverted_index):
    if term in inverted_index:
        return len(inverted_index[term])
    else:
        return 0

def inverse_document_frequency(term, inverted_index, total_documents):
    df = document_frequency(term, inverted_index)

    if df != 0:
        return math.log(total_documents / df)
    else:
        return 0

def term_frequency(term, inverted_index, documentID):
    if term in inverted_index:
        if documentID in inverted_index[term]:
            return inverted_index[term][documentID]
    
    return 0

def tf_idf(term, documentID, inverted_index, total_documents):
    tf = term_frequency(term, inverted_index, documentID)
    idf = inverse_document_frequency(term, inverted_index, total_documents)

    result = tf * idf

    return result

def document_vector(documentID, inverted_index, total_documents, vocabulary):
    doc_vector = []

    for t in vocabulary:
        tf_idf_weight = tf_idf(t, documentID, inverted_index, total_documents)
        doc_vector.append(tf_idf_weight)
    
    return doc_vector

def query_vector(query, inverted_index, total_documents, vocabulary):
    terms = tokenizer(query)

    qry_vector = []

    for t in vocabulary:
        tf = terms.count(t)
        idf = inverse_document_frequency(t, inverted_index, total_documents)

        qry_vector.append(tf * idf)
    
    return qry_vector

def cosine_similarity(qry_vector, doc_vector):
    dp = 0

    for i in range(len(qry_vector)):
        dp += qry_vector[i] * doc_vector[i]
    
    qry_magnitude = math.sqrt(sum(i**2 for i in qry_vector))
    doc_magnitude = math.sqrt(sum(i**2 for i in doc_vector))

    result = qry_magnitude * doc_magnitude

    if result == 0:
        return 0
    else:
        return (dp / result)

def rank_retrieval(query, inverted_index, total_documents, vocabulary, documentIDs):
    qry_vector = query_vector(query, inverted_index, total_documents, vocabulary)

    final_index = []

    for i in documentIDs:
        doc_vector = document_vector(i, inverted_index, total_documents, vocabulary)

        cosineSimilarity = cosine_similarity(qry_vector, doc_vector)
        final_index.append((i, cosineSimilarity))
    
    final_index.sort(key=lambda i: i[1], reverse=True)

    return final_index
