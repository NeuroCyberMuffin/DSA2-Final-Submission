#DSA2 Question 2

import networkx as nx
import matplotlib.pyplot as plt

# Create the original graph
Graph = nx.Graph()

# Adding  weighted edges
Graph.add_weighted_edges_from([
    ("A", "B", 5),
    ("A", "C", 4),
    ("A", "D", 8),
    ("B", "C", 3),
    ("B", "D", 6),
    ("B", "E", 7),
    ("C", "D", 3),
    ("C", "E", 4),
    ("C", "F", 7),
    ("D", "E", 5),
    ("E", "F", 3)
])

print("Original Graph")
print("Number of nodes=", Graph.number_of_nodes())
print("Number of edges=", Graph.number_of_edges())
print("Is connected=", nx.is_connected(Graph))

# Visualise the original graph using Matplotlib
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(Graph, seed=42)
nx.draw(
    Graph,
    pos,
    with_labels=True,
    node_color="orchid",
    node_size=1300,
    font_size=11
)

nx.draw_networkx_edge_labels(
    Graph,
    pos,
    edge_labels=nx.get_edge_attributes(Graph, "weight")
)
plt.suptitle("Original Weighted Graph", fontsize=16)
plt.show()


# Prim's Minimum Spanning Tree algorithm
def MyMinimumSpanningTree(Graph) -> nx.Graph:
    #  empty graph
    MST = nx.Graph()

    # Start from node A
    start_node = list(Graph.nodes())[0]

    # Add the starting node
    MST.add_node(start_node)
    print ("The starting node is = " , start_node)
    # Keep track of visited nodes
    visited = {start_node}
    visited_order = [start_node]
    print("_-_-_-_-_ Begin MST Construction _-_-_-_-")

    i=0
    # Continue until all nodes are included
    while len(visited) < len(Graph.nodes()):
        minimum_edge = None
        minimum_weight = float("inf")
        print("Step", i + 1, "Visited nodes:- ", visited_order)

        # check edges connected to visited nodes
        for node in visited:

            for neighbour in Graph.neighbors(node):

                # Consider only unvisited neighbours
                if neighbour not in visited:

                    weight = Graph[node][neighbour]["weight"]

                    # Select the lowest-weight edge
                    if weight < minimum_weight:
                        minimum_weight = weight
                        minimum_edge = (node, neighbour)


        #if no valid edge is foun graph is not connected    
        if minimum_edge is None:
            raise ValueError("The graph is not connected. MST cannot be constructed.")

        # Add the selected edge to the MST
        if minimum_edge is not None:

            u, v = minimum_edge

            MST.add_edge(u, v, weight=minimum_weight)
            visited.add(v)
            visited_order.append(v)

            # Show the selected edge
            print("Selected edge:", u, "-", v,"Weight is = ", minimum_weight)
            print("Current MST edges:")

            
            #show MST edges 
            for x, y, data in MST.edges(data=True):
                print(x, "-", y, "Weight =", data["weight"])

            print("......................................")
            
            i += 1

    print("\n ***MST construction completed!***")
    
    # Validate the MST
    if MST.number_of_nodes() != Graph.number_of_nodes():
        raise ValueError("MST does not have all original nodes.")

    if MST.number_of_edges() != Graph.number_of_nodes() - 1:
        raise ValueError("MST does not have the correct number of edges.")

    if not nx.is_connected(MST):
        raise ValueError("The resulting MST is not connected.")

    print("\nMST validation successful!")

    return MST

# Run Prim's algorithm
print("*******PRIM'S ALGORITHM********")

MST = MyMinimumSpanningTree(Graph)

print("MST edges:-")
for u, v, data in MST.edges(data=True):
    print(u, "-", v, "Weight = ", data["weight"])

print("Total MST weight = ",
      sum(data["weight"] for u, v, data in MST.edges(data=True)))

print("Number of MST edges = ", MST.number_of_edges())

# Visualise the Minimum Spanning Tree
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(Graph, seed=42)
nx.draw(
    MST,
    pos,
    with_labels=True,
    node_color="orchid",
    node_size=1500,
    font_size=12
)
nx.draw_networkx_edge_labels(
    MST,
    pos,
    edge_labels=nx.get_edge_attributes(MST, "weight")
)
plt.suptitle("MST for Prim's Algorithm", fontsize=16)
plt.show()

#*********************** GRAPH 2 ***********************
# Create the 2nd graph
Graph2 = nx.Graph()

# Adding  weighted edges
Graph2.add_weighted_edges_from([
    ("A", "B", 8),
    ("A", "D", 5),
    ("A", "C", 6),
    ("B", "C", 7),
    ("B", "F", 9),
    ("C", "D", 6),
    ("C", "E", 5),
    ("D", "F", 6),
    ("E", "F", 9),
    ("B", "E", 10),
    ("D", "E", 11)
])

print("Original Graph2")
print("Number of nodes=", Graph2.number_of_nodes())
print("Number of edges=", Graph2.number_of_edges())
print("Is connected=", nx.is_connected(Graph2))

# Visualise the original graph using Matplotlib
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(Graph2, seed=42, k=1.5, iterations=100)
nx.draw(
    Graph2,
    pos,
    with_labels=True,
    node_color="mediumturquoise",
    node_size=1500,
    font_size=11
)

nx.draw_networkx_edge_labels(
    Graph2,
    pos,
    edge_labels=nx.get_edge_attributes(Graph2, "weight"),
    font_size=11,
    rotate=False,
    label_pos=0.5
)
plt.suptitle("Original Weighted Second Graph", fontsize=16)
plt.show()

# Run Prim's algorithm
print("*******PRIM'S ALGORITHM FOR GRAPH 2********")

MST2 = MyMinimumSpanningTree(Graph2)

print("MST2 edges:-")
for u, v, data in MST2.edges(data=True):
    print(u, "-", v, "Weight = ", data["weight"])

print("Total MST2 weight = ",
      sum(data["weight"] for u, v, data in MST2.edges(data=True)))

print("Number of MST2 edges = ", MST2.number_of_edges())

# Visualise the Minimum Spanning Tree
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(Graph2, seed=42, k=1.5, iterations=100)
nx.draw(
    MST2,
    pos,
    with_labels=True,
    node_color="teal",
    node_size=1500,
    font_size=12
)
nx.draw_networkx_edge_labels(
    MST2,
    pos,
    edge_labels=nx.get_edge_attributes(MST2, "weight")
)
plt.suptitle("MST 2 for Prim's Algorithm", fontsize=16)
plt.show()

#*********************** GRAPH 3 ***********************
Graph3 = nx.Graph()
Graph3.add_weighted_edges_from([
    ("A", "B", 8),
    ("A", "C", 5),
    ("A", "D", 10),
    ("B", "C", 7),
    ("B", "E", 6),
    ("B", "F", 11),
    ("C", "D", 4),
    ("C", "G", 9),
    ("D", "E", 8),
    ("D", "H", 10),
    ("E", "F", 5),
    ("E", "G", 7),
    ("F", "G", 9),
    ("F", "I", 6),
    ("G", "H", 5),
    ("G", "J", 12),
    ("H", "I", 7),
    ("I", "J", 4)
])

print("Original Graph3")
print("Number of nodes=", Graph3.number_of_nodes())
print("Number of edges=", Graph3.number_of_edges())
print("Is connected=", nx.is_connected(Graph3))

# Visualise the original graph using Matplotlib
plt.figure(figsize=(12, 10))
pos = nx.spring_layout(Graph3, seed=42, k=1.5, iterations=100)
nx.draw(
    Graph3,
    pos,
    with_labels=True,
    node_color="purple",
    node_size=1600,
    font_size=12
)

nx.draw_networkx_edge_labels(
    Graph3,
    pos,
    edge_labels=nx.get_edge_attributes(Graph3, "weight"),
    font_size=11,
    rotate=False,
    label_pos=0.5
)
plt.suptitle("Original Weighted Third Graph", fontsize=16)
plt.show()

# Run Prim's algorithm
print("*******PRIM'S ALGORITHM FOR GRAPH 3********")

MST3 = MyMinimumSpanningTree(Graph3)

print("MST3 edges:-")
for u, v, data in MST3.edges(data=True):
    print(u, "-", v, "Weight = ", data["weight"])

print("Total MST3 weight = ",
      sum(data["weight"] for u, v, data in MST3.edges(data=True)))

print("Number of MST3 edges = ", MST3.number_of_edges())

# Visualise the Minimum Spanning Tree
plt.figure(figsize=(14, 12))
pos = nx.spring_layout(Graph3, seed=42, k=1.5, iterations=100)
nx.draw(
    MST3,
    pos,
    with_labels=True,
    node_color="lavender",
    node_size=1500,
    font_size=12
)
nx.draw_networkx_edge_labels(
    MST3,
    pos,
    edge_labels=nx.get_edge_attributes(MST3, "weight")
)
plt.suptitle("MST 3 for Prim's Algorithm", fontsize = 16)
plt.show()












