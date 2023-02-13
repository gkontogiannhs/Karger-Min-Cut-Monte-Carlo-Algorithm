import random
import numpy as np
from copy import deepcopy


def gnp_adjacency_matrix(n, p):

    # initialize a zero nxn matrix
    adj_matrix = np.zeros(shape=(n, n), dtype=int)

    # for every cell except from diagonal
    for i in range(n):
        for j in range(i + 1, n):
            # choose if edge exists with probability p
            adj_matrix[i][j] = adj_matrix[j][i] = np.random.choice([0, 1], p=[1-p, p])

    return adj_matrix


def krager_min_cut(graph):

    # Number of vertices
    n = len(graph)

    # Minimum cut found so far
    min_cut = float('inf')
    
    # Store the two disjoint sets
    min_cut_sets = (None, None)

    # Repeat the procedure n^2*log(n) times
    for _ in range(int(n * n * np.log(n))):

        # initialize adj matrix for each iteration
        cur_graph = deepcopy(graph)

        # enumerate vertices
        vertices = [i for i in range(n)]

        # repeat until there are only two vertices left 
        while len(vertices) > 2:

            # pick a random vertex
            u = random.choice(vertices)

            # find neigbors of u
            neighbors = [j for j in range(n) if cur_graph[u][j]]

            # pick a random neigbor of u
            v = random.choice(neighbors)

            # start the edge contracting procedure
            cur_graph[u][v] = cur_graph[v][u] = 0 # cut the edge between u and v

            # for each vertex
            for w in vertices:
                # if edge exists with vertex u
                if cur_graph[w][u]:

                    # attach this edge to v (by calculating the new edge weight)
                    cur_graph[w][v] += cur_graph[w][u]

                    # assign v as the super node
                    cur_graph[v][w] = cur_graph[w][v]

            # remove vertex u
            vertices.remove(u)

        # cut = sum(cur_graph[vertices[0]][j] for j in vertices[1:])
        # Count the number of edges crossing the cut
        cut = sum(cur_graph[vertices[0]][j] for j in range(n) if j not in vertices)
        
        # Update the minimum cut and the corresponding disjoint sets
        if cut < min_cut:
            min_cut = cut
            min_cut_sets = (vertices, [i for i in range(n) if i not in vertices])

    return min_cut, min_cut_sets




def min_cut_random_walks(graph):

    # Number of vertices
    n = len(graph)

    # Minimum cut found so far
    min_cut = float('inf')

    # Store the two disjoint sets
    min_cut_sets = (None, None)

    # Repeat the procedure multiple times
    for _ in range(n * n):
        # Choose a random vertex as the starting point for the cut
        start = random.randint(0, n - 1)
        side = [start]
        visited = [start]

        # Perform random walks
        for _ in range(n - 1):
            current = np.random.choice(side)
            neighbors = [j for j in range(n) if graph[current][j]]
            next_vertex = np.random.choice(neighbors)
            if next_vertex not in visited:
                side.append(next_vertex)
                visited.append(next_vertex)
            elif next_vertex in side:
                side.remove(next_vertex)

        # Count the number of edges crossing the cut
        cut = sum(graph[i][j] for i in side for j in range(n) if j not in side)

        # Update the minimum cut and the corresponding disjoint sets
        if cut < min_cut:
            min_cut = cut
            min_cut_sets = (side, [i for i in range(n) if i not in side])

    # Return the minimum cut
    return min_cut, min_cut_sets