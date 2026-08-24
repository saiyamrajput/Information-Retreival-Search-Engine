from preprocessing import tokenizer
import string

def single_term_retrieval(term, inverted_index):
    if term in inverted_index:
        return list(inverted_index[term])
    else:
        return []

def and_multiple_terms_retrieval(terms, inverted_index):
    if not terms:
        print("The given terms list is empty\n[]")
        return []
    
    result = set(single_term_retrieval(terms[0], inverted_index))

    for t in terms[1:]:
        document_numbers = single_term_retrieval(t, inverted_index)
        result = result.intersection(document_numbers)

    return list(result)

def or_multiple_terms_retrieval(terms, inverted_index):
    if not terms:
        print("The given terms list is empty\n[]")
        return []
    
    result = set(single_term_retrieval(terms[0], inverted_index))

    for t in terms[1:]:
        document_numbers = single_term_retrieval(t, inverted_index)
        result = result.union(document_numbers)

    return list(result)

def search(query, operator, inverted_index):
    query = tokenizer(query)
    operator = operator.upper()

    if operator == "AND":
        return and_multiple_terms_retrieval(query, inverted_index)
    elif operator == "OR":
        return or_multiple_terms_retrieval(query, inverted_index)
    else:
        return []