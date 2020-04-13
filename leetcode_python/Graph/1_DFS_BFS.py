# define a graph
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
# graph={
#     'A':['B','C'],
#     'B':['A','C','D'],
#     'C':['A','B','D','E'],
#     'D':['B','C','E','F'],
#     'E':['C','D'],
#     'F':['D']
# }

# N = [
#     {'B','C'},
#     {'A','C','D'},
#     {'A','B','D','E'},
#     {'B','C','E','F'},
#     {f},
#     {c, g, h},
#     {f, h},
#     {f, g}
# ]

def dfs(graph, start, visited):
    # path =  []   # use set to store the visited points
    visited.append(start)

    neighbors = graph[start]
    for next in neighbors:
        if next not in visited:
            # visited.append(next)
            dfs(graph, next, visited)
    return visited

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


# Tarversal
visited = []
path = dfs(graph, 'A', visited)
print("DFS: ",path)

visited_2 = []
path_BFS = bfs(graph, 'A', visited_2)
print("BFS: ",path_BFS)
