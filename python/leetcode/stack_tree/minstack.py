class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        元组+栈的方式
        """

        self.a = []

    def push(self, x: int) -> None:
        if not self.a:
            self.a.append((x,x))   # 调用元组存储最小值
        else:
            self.a.append((x, min(x, self.a[-1][1])))

    def pop(self) -> None:
        if self.a: self.a.pop()

    def top(self) -> int:
        if self.a:  return self.a[-1][0]
        else: return None

    def getMin(self) -> int:
        if self.a:  return self.a[-1][1]
        else: return None


# Your MinStack object will be instantiated and called as such:
obj = MinStack()

obj.push(9)
obj.push(5)

obj.push(6)
obj.pop()
print(obj.a)
# print(obj.pop())
param_3 = obj.top()
param_4 = obj.getMin()
print(param_3, param_4)