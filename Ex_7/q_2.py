import networkx as nx
import numpy as np
import networkx.algorithms.approximation.clique as cq
import matplotlib.pyplot as plt

# credit: https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.approximation.clique.max_clique.html

"""
The algorithm that i choose, is a Max Clique:
A clique in an undirected graph G = (V, E) is a subset of the vertex set C subset V 
such that for every two vertices in C there exists an edge connecting the two. 
This is equivalent to saying that the subgraph induced by C is complete (in some cases, 
the term clique may also refer to the subgraph).

A maximum clique is a clique of the largest possible size in a given graph.
The clique number omega(G) of a graph G is the number of vertices in a maximum clique in G.
The intersection number of G is the smallest number of cliques that together cover all edges of G.

The approximation ratio is O(|V|/(log|V|)^2) apx of maximum clique/independent set
in the worst case.

"""

# credit: geeksforgeeks
# exactly algorithm for calculate the approximation ratio
MAX = 100
n = 0
# Stores the vertices
store = [0] * MAX
# Graph
graph = [[0 for i in range(MAX)] for j in range(MAX)]
d = [0] * MAX


# check if the given set of vertices in store array is a clique
def is_clique(b):
    for i in range(1, b):
        for j in range(i + 1, b):
            if graph[store[i]][store[j]] == 0:
                return False
    return True


# Function to find all the sizes of maximal cliques
def maxCliques(i, l):
    max_ = 0
    for j in range(i + 1, n + 1):
        store[l] = j
        if is_clique(l + 1):
            # Update
            max_ = max(max_, l)
            max_ = max(max_, maxCliques(j, l + 1))
    return max_


# if __name__ == '__main__':
    # edges = [[1, 2], [2, 3], [3, 1],
    #          [4, 3], [4, 1], [4, 2]]
    # size = len(edges)
    # n = 4
    #
    # for i in range(size):
    #     graph[edges[i][0]][edges[i][1]] = 1
    #     graph[edges[i][1]][edges[i][0]] = 1
    #     d[edges[i][0]] += 1
    #     d[edges[i][1]] += 1

    # print(maxCliques(0, 1))
