from min_cut import krager_min_cut, gnp_adjacency_matrix, find_cut_random_walks
import networkx as nx
from matplotlib import pyplot as plt


if __name__ == '__main__':
    
    n = 100 # number of nodes
    p = 0.3 # probability of having an edge

    # Generate an adjacency matrix
    graph = gnp_adjacency_matrix(n, p)

    cut_size, disjoint_sets = krager_min_cut(graph)
    print(cut_size)
    print(disjoint_sets)

    graph = nx.from_numpy_matrix(graph)
    nx.draw(graph, with_labels=True)
    plt.show()