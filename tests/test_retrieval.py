import sys
sys.path.append("src")

from retrieval import single_term_retrieval, and_multiple_terms_retrieval, or_multiple_terms_retrieval, search
from preprocessing import tokenizer, inverted_index, load

inverted_index_single_term = {
    "wing": {1: 3, 4: 1, 7: 2},
    "air": {2: 1, 5: 3}
}

inverted_index_multiple_terms = {
    "wing": {1: 3, 4: 1, 7: 2},
    "air": {2: 1, 4: 3, 7: 1},
    "flow": {4: 2, 7: 1},
}

query = "wing and air and flow"

# single term retrieval
print(single_term_retrieval("wing", inverted_index_single_term))
print(single_term_retrieval("air", inverted_index_single_term))
print(single_term_retrieval("computer", inverted_index_single_term))

# multiple term retrieval
# Tokenizing
terms = tokenizer(query)

print("Query:", query)
print("Tokenized query:", terms)


result1 = and_multiple_terms_retrieval(terms, inverted_index_multiple_terms)
result2 = or_multiple_terms_retrieval(terms, inverted_index_multiple_terms)

print("Retrieved documents using query and:", result1)
print("Retrieved documents using query or:", result2)


# search wrapper
print(search(query, "AND", inverted_index_multiple_terms))
print(search(query, "OR", inverted_index_multiple_terms))

# missing term
print(search("wing and computer", "AND", inverted_index_multiple_terms))
print(search("wing or computer", "OR", inverted_index_multiple_terms))

#####################
# Cranfield
#####################

inverted_index_search = inverted_index(load("cran/cran.all.1400"))

result_for_and = search("wing flow", "AND", inverted_index_search)
result_for_or = search("wing flow", "OR", inverted_index_search)

print("wing flow AND:")
print(result_for_and)

print("\nwing flow OR:")
print(result_for_or)
