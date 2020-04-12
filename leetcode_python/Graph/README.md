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

**Definition** Depth First Search is used to explore nodes and edges of  graph. O(V+E)， the size of the graph .

It has good performance for problems such as count connected components, determine connectivity, find points ...

backtrack when the node is visited

```python
# DFS traversal
n = number of nodes in the graph
g = adjacency list representing graph
visited = [false, false....] # size the n, initialize

def dfs(points):
    if visited[points]:   return
    visited[points]=True
    
    neighbors  = graph[points]
    for next in neighbors:
        dfs(next)   # visit the adjacent node
    
 # start DFS at node zero
start_node = 0
dfs(stat_node)
```

```python
# find components
n = number of nodes in the graph
g = adjacency list representing graph
visited = [false, false....] # size n, initialize
count = 0
components = empty integer array

def findComponents():
    for i in n:
        if !visited[i]:
            count += 1    # record the start node
            dfs(i)
    return (count, components)

def dfs(at):
    visited[at] = True
    components[at] = count  # start node to the node in the neighbors 
    for next in g[at]:
        if !visited[next]:
            dfs(next)
```

# BFS

**Definition** Breadth First Search, O(V+E), which is often used as a building block in other algorithms and **finding the shortest path on unweighted graph**. Visited neighbors first, use **Queue**

```python
# BFS traaversal
n = number of nodes in the graph
g = adjacency list representing graph

# s = start, e = end
def bfs(s, e):
    # bfs at node s
    prev = solve(s)
    # return reconstructed path from s->e
    return reconstructPath(s,e,prev)

def solve(s):
    q = queue data structure with enqueue and dequeue
    q.enqueue(s)
    
    visited = [false, false....] # size n, initialize
    visited[s] = True
    
    prev = [null, null,...,null]	# size n
    while !q.isEmpty():
        node = q.dequeue()
        neighbors = g.get(node)
        
        for next in neighbors:
            if !visited[next]:
                q.enqueue(next)
                visited[next] = true
                prev[next] = node
        return prev
    
def reconstructPath(s, e, prev):
    path = []
    # backwards e->s the s->e
    for(at=e; at!=null;at=prev[at]):
        path.add(at)
    path.reverse()
    
    # if s and e connected
    if path[0] == s:
        return path
    return []
```

## BFS in grid

**Graph on Grds** 

![image-20200412094059163](C:\Users\liu\AppData\Roaming\Typora\typora-user-images\image-20200412094059163.png)

