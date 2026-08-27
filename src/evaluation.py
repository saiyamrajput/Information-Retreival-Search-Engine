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

def load_qrels(file_path):
    qrel = {}

    with open(file_path, "r") as file:
        for line in file:
            qry_ID, doc_ID, grade = line.split()

            qry_ID = int(qry_ID)
            doc_ID = int(doc_ID)
            grade = int(grade)

            if grade > 0:
                if qry_ID not in qrel:
                    qrel[qry_ID] = set()
            
                qrel[qry_ID].add(doc_ID)
    
    return qrel
