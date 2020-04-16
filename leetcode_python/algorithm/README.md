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

**Question**  Every time ask yourself. Most is about Shortest 

![image-20200411210539268](https://github.com/SamLiu666/CS-learning-Notes/raw/master/picture%20for%20markdown/leetcode_python/algorithm/graph%201%20(1).png)

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
# Uniformed Search

**choose the smaller cost and try** : *BFS	DFS	Uniform-cost Search	Iterative Deepening Search*
![image-20200416084642260](https://github.com/SamLiu666/CS-learning-Notes/raw/master/picture%20for%20markdown/leetcode_python/algorithm/my%20grah%20for%20bfs%20dfs%20.png)

## DFS

**Definition** Depth First Search is used to explore nodes and edges of  graph. O(V+E)

## BFS

**Definition** : Breadth First Search is search all the points level by level

```python
from collections import deque

n = ['A','B','C','D','E','F']
graph={
    'A':['B','C'],
    'B':['A','C','D'],
    'C':['A','B','E'],
    'D':['B','E','F'],
    'E':['C','D'],
    'F':['D']
}


def bfs(graph, start, visited):
    q = deque()   # define a queue structure
    q.append(start)
    visited.append(start)

    while q:
        node = q.popleft()
        neighbors = graph[node]

        for next in neighbors:
            if next not in visited:
                q.append(next)
                visited.append(next)
    return visited
    
visited_2 = []
path_BFS = bfs(graph, 'A', visited_2)
print("BFS: ",path_BFS)


tree = graph
def bfs_find(array): # start
    global tree
    index = 0
    node_layers = [['A']]
    solution = ['F']  # goal
    current_target = 'F'

    # get all the sequence
    while 'F' not in array:
        temp = []
        for item in tree[array[index]]:
            if item in array:
                continue
            temp.append(item) # sava node of layer
            array.append(item)
            if item == 'F':
                break
        node_layers.append(temp)
        index += 1

    # get optimal trace
    for i in range(index-1, 0, -1):
        for j in range(len(node_layers[i])):
            if current_target in tree[node_layers[i][j]]:
                current_target = node_layers[i][j]
                solution.append(node_layers[i][j])
                break
    solution.append('A')
    solution.reverse()
    return solution, array

solution, nodesvisited = bfs_find(['A'])
print("Op solution: ", str(solution))
print("Visited: ", str(nodesvisited))
```

###  Applications

1. Shortest path in a graph: the smallest distance 
2. Web crawler: start from source page
3. Social network: use the given distance 'k' to search the person relationship
4. Detecting a cycle in undirected graph
5. Check if graph is bipartite or not
6. Broadcasting in a Network
7. Ford-Fulkerson Algorithm: determine maximum flow in a flow network

## IDS

**Iterative Deepening Search** : layer by layer, backtrack and find goal,  kind like BFS+DFS in a layer

# Informed Search
Gready best-first search, A search, A* search, IDA* Search

![A star ](https://raw.githubusercontent.com/SamLiu666/CS-learning-Notes/master/picture%20for%20markdown/leetcode_python/algorithm/A%20star%20.png)


## Best-first greedy search

**Definition** : make locally optimal choice at each stage with the hope of finding a global optimum

**constrains**:  Greedy-choice property, optimal substructure


## Dijkstras 's Algorithm

It is a single source shortest path algorithm for graphs with non-negative edge weights. O(E*log(v))

**constrains** : graph must only contain non-negative edge weights

![image-20200413094528176](https://github.com/SamLiu666/CS-learning-Notes/raw/master/picture%20for%20markdown/leetcode_python/algorithm/dj1%20(1).png)



