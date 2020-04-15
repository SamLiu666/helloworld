"""图的显示方法"""

# 1.矩阵显示
graph_1 = [
    [0,1,0,0,1],
    [1,0,1,1,1],
    [0,1,0,1,0],
    [0,1,1,0,1],
    [1,1,0,1,0]
]


# 2. 相邻列表显示，以链表的形式存储边
class AdjNode:
    def __init__(self, data):
        self.vertex  = data
        self.next = None


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V

        # Function to add an edge in an undirected graph

    def add_edge(self, src, dest):
        # Adding the node to the source node
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        # Adding the source node to the destination as
        # it is the undirected graph
        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

        # Function to print the graph

    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex head {}\n {}".format(i, i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")


# Driver program to the above graph class
if __name__ == "__main__":
    V = 5
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    graph.print_graph()
    print("***********************")
    for i in range(len(graph_1)):
        print(graph_1[i])