from collections import Counter
from heapq import heappush, heappop
# 641 Design Circular Deque
class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.cique = [-1]*k
        self.size, self.capicity = 0, k
        self.front_, self.rear_ = 0, 0

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():   return False
        if self.isEmpty():  self.cique[self.front_] = value
        else:
            self.front_ = (self.front_-1) % self.capicity   # 数组最后一个
            # self.front_ = self.capicity-1
            self.cique[self.front_] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():   return False
        if self.isEmpty():  self.cique[self.rear_] = value
        else:
            self.rear_ = (self.rear_+1) % self.capicity # 末尾
            #self.rear_ = self.rear_ +1
            self.cique[self.rear_] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():  return False
        self.cique[self.front_] = -1
        self.front_ = (self.front_ + 1) % self.capicity     # 变为0
        self.size -= 1
        if self.isEmpty():
            self.rear_ = self.front_
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():  return False
        self.cique[self.rear_] = -1
        self.rear_ = (self.rear_ - 1) % self.capicity
        self.size -= 1
        if self.isEmpty():
            self.front_ = self.rear_
        return True


    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        return self.cique[self.front_]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        return self.cique[self.rear_]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        if self.capicity == self.size:
            return True
        else:
            return False
# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()

def leastInterval(tasks, n):
    curr, h = 0, []
    for k, v in Counter(tasks).items():
        heappush(h)
    pass