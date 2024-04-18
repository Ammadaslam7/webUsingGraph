import networkx as nx
import matplotlib.pyplot as plt

# Function to read data from a plain text file
def read_data(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text
    except Exception as e:
        print(f"Error reading data from file: {e}")
        return None


# Function to create a directed graph from the list of tokens
def create_directed_graph(tokens):
    try:
        G = nx.DiGraph()
        for i in range(len(tokens) - 1):
            source = tokens[i]
            target = tokens[i + 1]
            G.add_edge(source, target)
        return G
    except Exception as e:
        print(f"Error creating directed graph: {e}")
        return None

def create_topic_graphs(topic):
    # File path of the document containing data
    for i in range(1, 16):
        file_path = f"..\\preprocessing\\{topic}\\Document {i}_final.txt"
        
        # Read data from the document
        text = read_data(file_path)
        if text is None:
            print("No data found")
            return
        
        # Tokenize the text
        tokens = text.split()  # Assuming the text is already tokenized
        
        # Create a directed graph
        G = create_directed_graph(tokens)
        if G is None:
            print("Graph creation failed")
            return
        
        # Visualize the directed graph
        plt.figure(figsize=(10, 6))
        nx.draw(G, with_labels=True, node_size=500, node_color='skyblue', font_size=10, font_weight='bold')
        plt.title("Directed Graph of Terms from Document")
        plt.savefig(f"{topic}\\Graph {i}.png")
        plt.close()

        print(f"Graph {i} has been created")
    
    print(f"All graphs for {topic} created")

# Main function
def main():
    create_topic_graphs("Business and Finance")
    create_topic_graphs("Fashion and Beauty")
    create_topic_graphs("Marketing and Sales")

if __name__ == "__main__":
    main()