import pandas as pd
import networkx as nx

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

from sklearn.feature_extraction.text import TfidfVectorizer

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

def vectorize_text(train_list, test_list):
    vectorizer = TfidfVectorizer()
    train_vec = vectorizer.fit_transform(train_list)
    test_vec = vectorizer.transform(test_list)
    return train_vec, test_vec