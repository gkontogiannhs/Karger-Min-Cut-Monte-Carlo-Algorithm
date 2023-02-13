## Karger-Min-Cut-Monte-Carlo-Algorithm

This is an implementation of Krager's randomized min-cut algorithm in Python. The algorithm is used to find the minimum cut in an undirected graph.
The algorithm works by contracting edges in the graph randomly and finding the minimum cut. The process is repeated multiple times to increase the chances of finding the global minimum cut. The number of repetitions is proportional to n^2 * log(n), where n is the number of vertices in the graph.
### Usage
The algorithm takes an adjacency matrix representation of the graph as input. Each element graph[i][j] represents the weight of the edge between vertices i and j. If there is no edge between i and j, the element should be set to 0.
```
graph = [[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]]
min_cut, min_cut_sets, min_cut_edges = find_cut(graph)
```

The output min_cut is the size of the minimum cut, and min_cut_sets is a tuple of two lists representing the two disjoint sets resulting from the cut. The min_cut_edges is a list of tuples representing the edges that were contracted in the graph.
