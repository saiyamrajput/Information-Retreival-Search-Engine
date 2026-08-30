import sys
sys.path.append("src")
from preprocessing import tokenizer, load, inverted_index, load_query

# tokenizer test
line = "Machine Learning is very useful!! Everyone should atleast try learning it"
t = tokenizer(line)
print("Tokenizer: ")
print(t)

# inverted index frequency count
docs_test = [
    {
        "Document ID": 1,
        "Title": "",
        "Author": "",
        "Text": "machine machine learning"
    },
    {
        "Document ID": 2,
        "Title": "",
        "Author": "",
        "Text": "machine learning"
    },
    {
        "Document ID": 3,
        "Title": "",
        "Author": "",
        "Text": "deep learning"
    }
]

index = inverted_index(docs_test)

print("\nInverted Index:")
print(index)

# document load and inverted index check using cranfield corpus
documents = load("cran/cran.all.1400")

if len(documents) != 1400:
    sys.exit("Data not properly loaded")

inverted_index_doc = inverted_index(documents)

if len(inverted_index_doc) <= 0:
     sys.exit("Empty Inverted Index")

# checking if correct number of frequency is being calcualted or not
terms = ["wing", "flow", "air"]
doc1 = documents[0]
doc_id = doc1["Document ID"]
tokens = tokenizer(doc1["Text"])

for term in terms:

    expected = tokens.count(term)
    calculated = inverted_index_doc.get(term, {}).get(doc_id, 0)

    print("\nTerm:", term)
    print("Expected:", expected)
    print("Calculated:", calculated)

    if expected == calculated:
        print("Correct Frequency Test passed")
    else:
        print("Correct Frequency Test failed")
    
# missing term
missing_value = "kkhg"
if missing_value in inverted_index_doc:
    print("Missing term Test Failed for missing value")
else:
   print("\nMissing term Test Passed\n{}")
    
# checking load query
queries = load_query("cran/cran.qry")

print("Number of queries:", len(queries))
print("Query 1:", queries[0])

assert len(queries) == 225

assert queries[2]["Query ID"] == 4

assert queries[0]["Text"].strip() == "what similarity laws must be obeyed when constructing aeroelastic models of heated high speed aircraft ."
