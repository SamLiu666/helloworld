# Graph

**Undirected graph**

**Directed graph**

**Weight graph**

**Tree** : a undirected graph without a circle

**Rooted Trees** : a tree with a designated root node where other nodes points to it. out-tree and in-tree

**DAG** : directed graphs with no cycles

**Bipartite graph** : u and v nodes math each other

# Graph Representation

**Adjacency Matrix** : use matrix to represent graph, O(node*node)

**Adjacency List** : use list and node , O(edges). edge list like [(C,A,4), (A,C,1), (B,C,2)... ]

**Question**  Every time ask yourself. Most is about Shortest **p**

![image-20200411210539268](C:\Users\liu\AppData\Roaming\Typora\typora-user-images\image-20200411210539268.png)

## Questions

| **Question**                         | Solution                                                     |
| ------------------------------------ | ------------------------------------------------------------ |
| Shortest path                        | BFS(unweighted graph), Dijkstra's, Bellman-Ford, Floyd-Warshall, A*, |
| Connectivity                         | Union find data structure or search algorithm like BFS       |
| Negative Cycles                      | Bellman_Ford and Floyd-Warshall                              |
| Strongly Connected Components (SCCs) | Tarjan's Kosaraju'S algorithm                                |
| Traveling Salesman                   | Held-Karp, branch and bound and approximation algorithm      |
| Minimum Spanning Tree(MST)           | Kruskal's, Prim's                                            |
| Network flow: max flow               | Ford_Fulkerson, Edmonds-Karp                                 |

# DFS

**Definition** Depth First Search is used to explore nodes and edges of  graph. O(V+E)