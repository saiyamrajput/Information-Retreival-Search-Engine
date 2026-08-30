import string
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

def load(file_path):
    doc_content = []
    doc = None
    doc_dictionary_key = None

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()

            if line.startswith(".I"):
                if doc is not None:
                    doc_content.append(doc)
                
                doc = { "Document ID": int(line.split()[1]),
                        "Title": "",
                        "Author": "",
                        "Text": ""
                    }
                doc_dictionary_key = None

            elif line == ".T":
                doc_dictionary_key = "Title"
            elif line == ".A":
                doc_dictionary_key = "Author"
            elif line == ".B":
                doc_dictionary_key = None
            elif line == ".W":
                doc_dictionary_key = "Text"
            elif (doc is not None and doc_dictionary_key is not None):
                doc[doc_dictionary_key] += line + " "
    
    if doc is not None:
        doc_content.append(doc)

    return doc_content

def load_query(file_path):
    queries = []
    query = None
    query_dictionary_key = None

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()

            if line.startswith(".I"):
                if query is not None:
                    queries.append(query)
                
                query = { "Query ID": int(line.split()[1]),
                          "Text": ""
                    }
                query_dictionary_key = None

            elif line == ".W":
                query_dictionary_key = "Text"
            elif (query is not None and query_dictionary_key is not None):
                query[query_dictionary_key] += line + " "

    if query is not None:
        queries.append(query)

    return queries

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

def tokenizer(string_of_words):

    # converting to lower case
    string_of_words = string_of_words.lower()

    # removing punctuations
    string_of_words = string_of_words.translate(str.maketrans("", "", string.punctuation))
    
    # splitting into tokens
    token = string_of_words.split()

    # removing stop words
    new_token = []
    for t in token:
        if t not in ENGLISH_STOP_WORDS:
            new_token.append(t)
    
    return new_token

def inverted_index(doc):
    inverted_index_dic = {}

    for d in doc:
        doc_id = d["Document ID"]
        doc_text_token = tokenizer(d["Text"])

        for t in doc_text_token:
            if t not in inverted_index_dic:
                inverted_index_dic[t] = {}

            if doc_id not in inverted_index_dic[t]:
                inverted_index_dic[t][doc_id] = 0
            
            inverted_index_dic[t][doc_id] += 1
    
    return inverted_index_dic
