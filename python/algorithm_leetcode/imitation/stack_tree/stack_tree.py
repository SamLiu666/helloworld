from matplotlib import collections

"""1、有效括号问题
2、用栈实现队列，FIFO，用两个栈实现
3、用队列实现栈，FILO，用collections 库实现
4、有效括号"""


class solution:

    def pro_1021(self, s):
        """输入n个括号，输出成对的括号"""
        res, par = [], 0
        for c in s:
            if c == '(' and par > 0: res.append(c)
            if c == ')' and par > 1: res.append(c)
            par += 1 if c == '(' else -1
        return "".join(res)

    def pro1021_1(self, s):
        res = []
        flag = 0
        for char in s:

            if char == '(' and flag > 0:
                res.append(char)
            if char == ')' and flag > 1:
                res.append(char)
            flag += 1 if char == '(' else -1
        return "".join(res)


"""栈实现队列,FIFO，用两个栈"""


class Myqueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int):
        # 入栈
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(x)
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def pop(self):
        # 出栈

        return self.stack1.pop()

    def peek(self):
        # 得到最开始的数据
        return self.stack1[-1]

    def empty(self):
        return not self.stack1


"""用队列实现栈"""


class Mystack:

    def __init__(self):
        self.stack = collections.deque([])

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.stack.append(x)

    # @return nothing
    def pop(self):
        for i in range(len(self.stack) - 1):
            self.stack.append(self.stack.popleft())

        self.stack.popleft()

    # @return an integer
    def top(self):
        return self.stack[-1]

    # @return an boolean
    def empty(self):
        return len(self.stack) == 0


# 树的定义，构造树
class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree_problem:

    # 617合并两个二叉树
    def mergeTrees(self, t1: TreeNode, t2: TreeNode):
        # t1 = TreeNode
        # t2 = TreeNode
        if (not t1): return t2
        if (not t2): return t1
        t1.val = t1.val + t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1

    # 104 二叉树的最大深度
    def maxDepth(self, root: TreeNode):
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # 226 翻转二叉树
    def invertTree(self, root: TreeNode):
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root

    # p 543 二叉树直径问题，二叉树遍历问题
    def diameteroftree(self, root: TreeNode):
        self.ans = 1

        def depth(node):
            if not node: return 0
            L = depth(node.left)
            R = depth(node.right)
            self.ans = max(self.ans, L + R + 1)
            return max(L, R) + 1

        depth(root)
        return self.ans - 1

    # p 101 对称树，检测一个二叉树是否对称
    def isSymmetric(self, root: TreeNode):

        def isTrue(l: TreeNode, r: TreeNode):
            if (l == None and r == None): return True
            if (l == None or r == None): return False
            if (l.val == r.val):
                if (isTrue(l.left, r.right) and isTrue(l.right, r.left)):
                    return True
            return False

        return isTrue(root, root)


s = solution()
tr = Tree_problem()
test = TreeNode
print(tr.diameteroftree(test))
# stest = "(())())"
# print(s.pro_1021(stest), s.pro1021_1(stest))
