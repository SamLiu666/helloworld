# Graph

**Undirected graph**

**Directed graph**

**Weight graph**

**Tree** : a undirected graph without a circle

**Rooted Trees** : a tree with a designated root node where other nodes points to it. out-tree and in-tree

**DAG** : directed graphs with no cycles

**Bipartite graph** : u and v nodes math each other

![image-20200412173032710](C:\Users\liu\AppData\Roaming\Typora\typora-user-images\image-20200412173032710.png)



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

![image-20200413094147155](C:\Users\liu\AppData\Roaming\Typora\typora-user-images\image-20200413094147155.png)



# BFS

**Definition** : Breadth First Search is search all the points level by level

![image-20200413094227392](C:\Users\liu\AppData\Roaming\Typora\typora-user-images\image-20200413094227392.png)

## Applications

1. Shortest path in a graph: the smallest distance 
2. Web crawler: start from source page
3. Social network: use the given distance 'k' to search the person relationship
4. Detecting a cycle in undirected graph
5. Check if graph is bipartite or not
6. Broadcasting in a Network
7. Ford-Fulkerson Algorithm: determine maximum flow in a flow network

# Dijkstras 's Algorithm

It is a single source shortest path algorithm for graphs with non-negative edge weights. O(E*log(v))

**constrains** : graph must only contain non-negative edge weights

![image-20200413094528176](C:\Users\liu\AppData\Roaming\Typora\typora-user-images\image-20200413094528176.png)

![image-20200413094959962](C:\Users\liu\AppData\Roaming\Typora\typora-user-images\image-20200413094959962.png)

![image-20200413095020671](C:\Users\liu\AppData\Roaming\Typora\typora-user-images\image-20200413095020671.png)

# Best-first greedy search

**Definition** : make locally optimal choice at each stage with the hope of finding a global optimum

**constrains**:  Greedy-choice property, optimal substructure