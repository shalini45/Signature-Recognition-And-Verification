
import string
import os
from gensim.parsing.preprocessing import remove_stopwords

# Pre-processing files
def pre_process(doc):
    temp = doc.lower()
    temp = temp.translate(str.maketrans('', '', string.punctuation + string.digits))
    temp = remove_stopwords(temp)
    return temp

# Jaccard Similarity Index
def jaccard_similarity(doc1, doc2):
    word_1 = set(doc1.split())
    word_2 = set(doc2.split())
    inter = word_1.intersection(word_2)
    union = word_1.union(word_2)
    return float(len(inter) / len(union))

# Read all summary files
# Calculating similarity between one file and the rest of the dataset
def print_similarity(x):
    docs = dict()
    directory = '/content/SignatureBasedDocumentRetrieval/Dataset/TXTs/'
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        with open(file_path, 'r', encoding="utf8") as f:
            temp = f.read()
            temp = pre_process(temp)
            docs[file_name] = temp
    print("----------------------------------------------------------")
    print("DOCUMENT SIMILARITY")
    print("----------------------------------------------------------")
    if x < 10:
        for key in docs.keys():
            print('Similarity of File :PES1PG22CS00'+str(x)+'.pdf with File : '+ key[:-4] + '.pdf is: ' + str(jaccard_similarity(docs['PES1PG22CS00'+str(x)+'.txt'], docs[key])))
    else:       
        for key in docs.keys():
            print('Similarity of File :PES1PG22CS0'+str(x)+'.pdf with File : '+ key[:-4] + '.pdf is: ' + str(jaccard_similarity(docs['PES1PG22CS0'+str(x)+'.txt'], docs[key])))
