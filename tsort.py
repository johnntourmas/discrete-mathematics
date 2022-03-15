import networkx as nx
import matplotlib.pyplot as plt
from random import randrange


def get_node_degree_zero(E):
    # a function which choose a random node of degree zero
    while True:
        # choose a possible node of degree zero
        node = E[randrange(0, len(E))][0]

        # check if this node has degree zero, a degree zero node has no connections
        is_degree_zero = True
        for edges in E:
            # to deftero keli tis upolistas tou E mas deixnei pou koitaei to velaki
            # an kanena velaki de koitaei tin korufi pou eksetazoume tote einai vathmoy miden
            if edges[1] == node:
                is_degree_zero = False
                break

        if is_degree_zero:
            return node


def typological_sort(E):
    g = nx.DiGraph()
    g.add_edges_from(E1)
    if nx.is_directed_acyclic_graph(g):
        L = []
        # while list is not empty
        while E:
            degree_zero_node = get_node_degree_zero(E)
            ####### for compile reasons ######
            print(E)
            print(degree_zero_node)
            # tin prosthetoume sti lista L
            L.append(degree_zero_node)
            # before delete the last node append it to the list
            if len(E) == 1:
                L.append(E[0][1])

            # afou pirame ti korufi me bathmo miden tote diagrafoume ti korufi kai ola ta toksa
            while True:
                exist = False
                for index, edges in enumerate(E):
                    if degree_zero_node in edges:
                        E.pop(index)
                for index, edges in enumerate(E):
                    if degree_zero_node in edges:
                        exist = True
                if exist == False:
                    break

        print(f"Typological layout: {L}")
        return L
    else:
        print("This graph is circular")
        return -1


# eisagwgi stoixeiwn grafimatos askisi 1.15
E = [[1, 8], [2, 6], [2, 9], [3, 8], [4, 1], [4, 9], [6, 1], [6, 8], [7, 5], [8, 7], [9, 8]]

# eisagwgi stoixeiwn grafimatos askisi 1.16
E2 = [[1,6], [1,9], [1,8], [1,3], [2,4], [3,8], [5,7], [5,1], [6,2], [7,1], [8,6], [8,4], [9,2], [9,4]]

# bohthitiko antigrafo gia emfanisi tou grafimatos
E1 = E[:]

# briskoume ti tupologiki diataksi
typological_sort(E)

# emfanizoume kai to grafima
# g = nx.DiGraph()
# g.add_edges_from(E1)
# nx.draw_networkx(g)
# plt.show()
