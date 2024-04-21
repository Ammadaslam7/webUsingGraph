import pandas as pd
import nltk
import networkx as nx

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

def preprocess_text(text):
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
    porter = PorterStemmer()
    stemmed_tokens = [porter.stem(word) for word in filtered_tokens]
    return stemmed_tokens

def create_graph(text):
    terms = preprocess_text(text)
    G = nx.DiGraph()
    for i in range(len(terms)-1):
        G.add_edge(terms[i], terms[i+1])
    return G

# Read CSV file
data = pd.read_csv("C:\BSCS6\webUsingGraph\csv\MergeCsv.csv", encoding='latin1')
print("Data loaded from CSV:")
print(data.head())  # Print first few rows of the DataFrame

# Select subset of data
data = pd.concat([data.iloc[0: 12], data.iloc[15:27], data.iloc[30:42]])

# Preprocess text and create graphs
content_column = 0
document_graphs = {}

for index, row in data.iterrows():
    content = row[content_column]
    document_id = index 
    
    # Preprocess text
    preprocessed_text = preprocess_text(content)
    print(f"Preprocessed text for document {document_id}:")
    print(preprocessed_text)  # Print preprocessed text
    
    # Create graph for the content
    document_graphs[document_id] = create_graph(content)

print("Document graphs:")
print(document_graphs)  # Print document graphs dictionary
