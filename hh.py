import networkx as nx
import matplotlib.pyplot as plt
from random import randrange

"""
FOR FAST COPY-PASTE
6, 6, 4, 4, 2, 2, 2, 2

1.2
5, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3
6, 3, 3, 3, 3, 2, 2, 2, 2, 2, 1 ,1


1.3
i) 11,10, 9, 8, 7, 6, 5, 4, 3, 2,1, 0
ii) 5, 5, 4, 4, 3, 3, 2, 2,1,1
iii) 5, 5, 3, 3, 3, 1
iv) 6, 3, 3, 3, 3, 3, 3
v) 3, 3, 3, 3,1,1,1,1,1,1 και το G να είναι συνεκτικό.
vi) 3, 3, 3, 3,1,1,1,1,1,1 και το G να μην είναι συνεκτικό.
vii) 3, 3, 3, 3, 2, 2, 2, 2, 2
viii) 4, 4, 2, 2, 2, 2, 2, 2, 2, 2 και το G να είναι συνεκτικό.
ix) 4, 4, 2, 2, 2, 2, 2, 2, 2, 2 και το G να μην είναι συνεκτικό.
"""

d = [5, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3]
a = d[:] # the sequence
v = [0 for i in d]

if nx.is_valid_degree_sequence_havel_hakimi(a): # check if the sequence is valid
    E = [] # the edges in the beginning are empty

    while True:
        # check if the values of the list ara all zero
        all_zero = True
        for value in a:
            if value != 0:
                all_zero = False
        # if all the values are zero then we break the loop
        if all_zero:
            break

        ############# add for compile reasons, if someone want to see tse steps of the algorithm #################
        print('------------start---------------')

        randomV = randrange(len(v))  # choose a random node > 0
        while a[randomV] <= 0:
            randomV = randrange(len(a))

        ############# add for compile reasons, if someone want to see tse steps of the algorithm #################
        print(f"a: {a}")
        print(f"E: {E}")
        print(f"randomV: {randomV}")

        # make the edges
        all_max = []
        while a[randomV] > 0:
            max_value = -1
            position = -1
            for index, value in enumerate(a):
                if value > max_value and randomV != index and index not in all_max and value > 0: # dont't match with the same values more than
                    position = index                                                              # 1 time, don't match with yourself and don't match with zeros
                    max_value = value
                    all_max.append(position)

            E.append([randomV,position]) # make the edges of the random choice with the max position of value of list a
            if a[randomV] > 0 and a[position] > 0:
                a[randomV] -= 1
                a[position] -= 1

        ############# add for compile reasons, if someone want to see tse steps of the algorithm#################
        print(f"a: {a}")
        print(f"E: {E}")
        print('------END LOOP-----------') # add for compile reasons, if someone want to see tse steps of the algorithm
    print('-----------------')
    print(f"a: {a}") # add for compile reasons, if someone want to see tse steps of the algorithm
    print(f"E: {E}")

    G = nx.Graph()
    G.add_edges_from(E)
    G.add_nodes_from(v)
    nx.draw_networkx(G)
    plt.show()
else:
    print("This graph doesn't exist")

