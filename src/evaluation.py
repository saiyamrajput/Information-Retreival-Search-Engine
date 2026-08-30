def precision_at_k(rankedList, relevantdocumentIDs, k):
    top_k = rankedList[: k]
    relevantDoc = 0

    for i, j in top_k:
        if i in relevantdocumentIDs:
            relevantDoc += 1
    
    if len(top_k) == 0:
        return 0

    return relevantDoc / k

def recall_at_k(rankedList, relevantdocumentIDs, k):
    top_k = rankedList[: k]
    relevantDoc = 0

    for i, j in top_k:
        if i in relevantdocumentIDs:
            relevantDoc += 1
    
    if len(relevantdocumentIDs) == 0:
        return 0

    return relevantDoc / len(relevantdocumentIDs)
