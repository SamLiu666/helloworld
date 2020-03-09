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
            if c=='(' and par > 0: res.append(c)
            if c==')' and par > 1: res.append(c)
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


class Myqueue:
    """栈实现队列,FIFO，用两个栈"""
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x:int):
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


class Mystack:
    """用队列实现栈"""
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


class problem:

    def pro_20(self, s):



s = solution()
stest = "(())())"
print(s.pro_1021(stest), s.pro1021_1(stest))