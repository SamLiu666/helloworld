class Node:

    def __init__(self, value, nextnode=None):
        # 初始化结点结构
        self.value = value
        self.next_node = nextnode

    def get_next(self):
        return self.next_node

    def set_next(self, nextnode):
        self.next_node = nextnode

    def get_data(self):
        return self.value

    def set_value(self, value):
        self.value = value


class LinkedList:
    def __init__(self, root=None):
        # 初始化链表数据结构
        self.root = root    # 默认是链表第一个结点
        self.size = 0

    def get_size(self):
        return self.size

    def add(self, node:Node):
        new_node = Node(node, self.root)
        self.root = new_node
        self.size += 1

    def remove(self, node:Node):
        this_node = self.root
        pre_node = None

        while this_node is not None:
            if this_node.get_data() == node:
                #r 如果不是第一个结点
                if pre_node is not None:
                    pre_node.set_next(this_node.get_next())
                else:
                    self.root = this_node.get_next()
                self.size -= 1
                return True
            else:
                pre_node = this_node
                this_node = this_node.get_next()
        return False

    def find(self, node:None):
        this_node = self.root
        while this_node is not None:
            if this_node.get_data() == node:
                return node
            elif this_node.get_next() == None:
                return False
            else:
                this_node = this_node.get_next()



if __name__ == '__main__':

    link = LinkedList()
    for i in range(5):
        link.add(i)
    print('size: ', link.size)
    print(link.remove(3))