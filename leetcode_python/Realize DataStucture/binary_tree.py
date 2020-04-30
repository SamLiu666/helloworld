class Node:

    def __init__(self, node):
        self.node = node
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.node)


class Tree:
    def __init__(self):
        self.root = Node('root')

    # 元素添加结点
    def add(self, item):
        node = Node(item)

        if self.root is None:
            self.root = node
        else:
            # 用列表存储
            q = [self.root]
            while True:
                pop_node = q.pop(0)

                # 左为空加左边
                if pop_node.left is None:
                    pop_node.left = node
                    return

                # 右为空 加到右边
                elif pop_node.right is None:
                    pop_node.right = node
                    return

                else:
                    q.append(pop_node.left)
                    q.append(pop_node.rihgt)