import networkx as nx
import matplotlib.pyplot as plt


def euler(n):
    if n % 2 == 0 and n > 0:
        print("Euler graph doesn't exist")
        return -1
    E = []
    cnt = 0
    while cnt < n:
        # αντιστοίχηση όλων των κορυφών μεταξύ τους
        for i in range(n):
            if i != cnt:
                E.append([cnt, i])
        cnt += 1
    return E


number = int(input('Give me a number: '))
edges = euler(number)

if edges != -1:
    G = nx.Graph()
    G.add_edges_from(edges)
    G.add_nodes_from(range(number))
    nx.draw_networkx(G)
    plt.show()