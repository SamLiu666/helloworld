# define a graph
from collections import deque


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


def bfs_find(array): # 起始点，用数组表示
    global tree  # 图的结构，设定为全局变量
    index = 0       # 访问的层级
    node_layers = [['A']]   # 初始层
    solution = ['F']    # 以目标初始化，作为节点
    current_target = 'F'  # 暂时目标，返回最后的路径

    # 得到访问点的序列
    while 'F' not in array:    # 目标不在数组中
        temp = []               # 临时数组，存储每一层的相邻节点
        for item in tree[array[index]]:
            if item in array:
                continue
            temp.append(item) # 存储这一层访问的点
            array.append(item)
            if item == 'F':
                break
        node_layers.append(temp)
        index += 1

    # 得到最优路径，倒序查找
    for i in range(index-1, 0, -1):         # 总层数
        for j in range(len(node_layers[i])):    # 子节点的个数
            ss = tree[node_layers[i][j]]
            if current_target in tree[node_layers[i][j]]:   # 子节点的所有结点找一遍
                current_target = node_layers[i][j]
                solution.append(node_layers[i][j])
                break
    solution.append('A')
    solution.reverse()
    return solution, array


def dfs_find(array):
    global visited_nodes, tree1
    ss = visited_nodes
    if set(tree1[array[-1]]).issubset(visited_nodes):   # 若为其子集，则路到了尽头，走不通，返回
        del array[-1]
        return dfs_find(array)

    for item in tree1[array[-1]]:
        if item in visited_nodes:
            continue
        visited_nodes.append(item)
        array.append(item)
        if item == 'F':
            return  visited_nodes,array
        else:
            return dfs_find(array)


if __name__ == '__main__':
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
    n = ['A', 'B', 'C', 'D', 'E', 'F']
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'E'],
        'D': ['B', 'E', 'F'],
        'E': ['C', 'D'],
        'F': ['D']
    }
    tree = graph
    tree1 = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'E'],
        'D': ['B', 'F'],
        'E': ['C'],
        'F': ['D']
    }
    # dfs Traversal
    visited = []
    path = dfs(graph, 'A', visited)
    print("DFS: ", path)

    # bfs Traversal
    visited_2 = []
    path_BFS = bfs(graph, 'A', visited_2)
    print("BFS: ", path_BFS)

    # DFS search path -- Graph change a little
    visited_nodes = ['A']
    solution_dfs, visited_nodes = dfs_find(['A'])
    print("DFS - Op solution: ", str(visited_nodes))
    print("DFS - Visited: ", str(solution_dfs))

    # BFS search path
    solution, nodesvisited = bfs_find(['A'])
    print("BFS - Op solution: ", str(solution))
    print("BFS - Visited: ", str(nodesvisited))