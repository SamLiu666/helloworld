from random import randint

class Node:
    def __init__(self, val):
        # initialize the node
        self.value = val
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        # 完成 树 类中添加元素的任务，二叉树，左边比结点小，右边比结点大
        if self.value == data:
            return False
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True
        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True

    def find(self, data):
        # 二叉树查找值
        if self.vale == data:
            return True
        elif self.value > data:
            if self.leftChild: return self.leftChild.find(data)
            else: return False
        else:
            if self.rightChild: return  self.rightChild.find(data)
            else: return False
        return False

    # 前序遍历
    def preorder(self):
        if self:
            # 先结点  再 左 最后 右
            print(str(self.value))
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()

    # 后序遍历
    def postorder(self):
        if self:
            # 先左再右 后结点
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print(str(self.value))

    # 顺序遍历
    def inorder(self):
        if self:
            # 先左 再结点 最后 右
            if self.leftChild:
                self.leftChild.inorder()
            print(str(self.value))
            if self.rightChild:
                self.rightChild.inorder()


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        # 建立二叉树
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def find(self, data):
        # 查找二叉树
        if self.root:
            return self.root.find(data)
        else:
            return False

    # 前序遍历
    def preorder(self):
        print("** PreOrder **")
        self.root.preorder()

    # 后序遍历
    def postorder(self):
        print("** PostOrder **")
        self.root.postorder()

    # 顺序遍历
    def inorder(self):
        print('** InOrder **')
        self.root.inorder()

if __name__ == '__main__':

    # 实现 二叉树
    bst = Tree()
    res = []
    # bst.insert(10)
    # print(bst.insert(15))
    for i in range(10):
        num = int(randint(1,20))
        res.append(num)
        bst.insert(num)
    print(res)
    bst.preorder()
    print('\n')
    bst.postorder()
    print('\n')
    bst.inorder()
