import pandas as pd
import networkx as nx
from collections import Counter
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

# Assuming you have these functions and variables defined
from data_helpers import create_graph, vectorize_text

# Function to compute the maximal common subgraph (MCS) between two graphs
def compute_mcs(G1, G2):
    return nx.intersection(G1, G2)

# Function to compute distance between two graphs based on MCS
def compute_distance(G1, G2):
    mcs_graph = compute_mcs(G1, G2)
    return 1 - len(mcs_graph)/max(len(G1), len(G2))

# Function to perform kNN classification
def graph_knn(train_graphs, train_categories, test_graph, k):
    distances = []

    # Compute distance between test_graph and each training graph
    for train_id, train_graph in enumerate(train_graphs):
        try:
            distance = compute_distance(test_graph, train_graph)
            distances.append((train_id, distance))
        except Exception as e:
            print(f"Error computing distance for train_id {train_id}: {e}")

    # Sort distances in ascending order
    distances.sort(key = lambda x: x[1])

    # Get the k-nearest neighbors
    neighbors = distances[:k]

    # Get categories of the neighbors
    neighbor_categories = list(map(lambda x: train_categories[x[0]], neighbors))

    # Find the majority class
    majority_class = Counter(neighbor_categories).most_common(1)[0][0]

    return majority_class

def vector_knn(X_train, y_train, X_test, k):
    knn_classifier = KNeighborsClassifier(n_neighbors=k)
    knn_classifier.fit(X_train, y_train)
    y_pred = knn_classifier.predict(X_test).tolist()
    return y_pred

try:
    # Read CSV file
    data = pd.read_csv("csv\MergeCsv.csv", encoding = 'latin1')
    # data = pd.read_csv("D:\Work\Semester 6\GT\Project 1\webUsingGraph\csv\MergeCsv.csv", encoding='latin1')

except FileNotFoundError:
    print("Error: 'merged_file.csv' not found. Please check the file path.")

# Extract columns
X = data['content'].tolist()
y = data['type'].tolist()
K = 3

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 42)

# Graph-based classification
# Convert contents into graphs
train_graphs = list(map(create_graph, X_train))
test_graphs = list(map(create_graph, X_test))

# Perform classification
y_pred = []
for test_graph in test_graphs:
    y_pred.append(graph_knn(train_graphs, y_train, test_graph, k = K))

# Print metrics
print("Graph-based kNN")
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))

# Vector-based classification
train_vectors, test_vectors = vectorize_text(X_train, X_test)
# Perform classification
y_pred = vector_knn(train_vectors, y_train, test_vectors, k = K)

# Print vector metrics
print("\n\nVector-based kNN")
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))