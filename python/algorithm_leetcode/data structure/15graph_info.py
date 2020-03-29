"""构造图的类，使用 列表方法adjacnt_list 如 'A': ['B', 'C',] ...."""


class Vertex:
    """定义顶点"""
    def __init__(self, n):
        # 初始化顶点，相邻的边用列表表示，易于操作
        self.name = n
        self.neighbors = []

    def add_neighbor(self, v):
        # 添加相邻边
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()


class Graph:

    vertices = {}    # 字典表示顶点，方便查询任意顶点

    def add_vertex(self, vertex):
        # 判断传入的对象是否是Vertex类，并且不在vertices 中，添加顶点
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:return False

    def add_edge(self, u, v):
        # 添加边
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:    value.add_neighbor(v)
                if key == v:    value.add_neighbor(u)
            return True
        else:
            return False

    def print_graph(self):
        # 打印图表
        for key in sorted(list(self.vertices.keys())):
            print(key+ " " + str(self.vertices[key].neighbors))


if __name__ == '__main__':
    # test program
    g = Graph()
    # print(str(len(g.vertices)))
    a = Vertex('A')
    g.add_vertex(a)
    g.add_vertex(Vertex('B'))

    for i in range(ord('A'),ord('K')):
        # ord() 函数是 chr() 函数（对于 8 位的 ASCII 字符串）的配对函数，它以一个字符串（Unicode 字符）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值。
        g.add_vertex(Vertex(chr(i)))

    edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FH', 'FJ', 'GJ', 'HI']
    # print(g.print_graph())
    for edge in edges:
        # g.add_edge(edge[:1], edge[1:])
        g.add_edge(edge[0], edge[1])
    g.print_graph()

# s = []
# s.append(11)
# print(s)
# output:
# A['B', 'E']
# B['A', 'F']
# C['G']
# D['E', 'H']
# E['A', 'D', 'H']
# F['B', 'H', 'J']
# G['C', 'J']
# H['D', 'E', 'F', 'I']
# I['H']
# J['F', 'G']