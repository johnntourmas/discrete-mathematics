import networkx as nx

G1 = nx.Graph()
G1.add_nodes_from(range(1, 8))
G1.add_edges_from(
    [[1, 2], [1, 3], [1, 6], [1, 7], [2, 3], [2, 7], [3, 4], [3, 7], [4, 5], [4, 6], [4, 7], [5, 6], [6, 7]])
G2 = nx.Graph()
G2.add_nodes_from(range(1, 8))
G2.add_edges_from(
    [[1, 2], [1, 5], [1, 4], [1, 6], [2, 3], [2, 6], [2, 7], [3, 4], [3, 6], [3, 7], [4, 5], [4, 6], [6, 7]])
# Test whether the graphs are isomorphic
GM = nx.isomorphism.GraphMatcher(G1, G2)
if GM.is_isomorphic():  # If G1 , G2 are isomorphic
    print("The graphs are isomorphic")
    print("An isomorphism between them is the following:")
    for i in G1:
        print("v", i, "->", "u", GM.mapping[i])
    print(GM.mapping)
else:
    print("The graphs are not isomorphic")
