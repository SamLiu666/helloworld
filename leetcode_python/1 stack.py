"""stack: https://leetcode.com/tag/stack/"""
from typing import List

# 225 Implement Stack using Queues
class MyStack:
    # 列表可以很好的完成栈的功能
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mystack = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.mystack.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """

        return self.mystack.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.mystack[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if len(self.mystack) == 0:
            return True
        else:
            return False

# 155 Min Stack
class MinStack:
    # 用栈和元组，才存储数据和最小值； 两个列表同样可行
    def __init__(self):
        self.minstack = []

    def push(self, x):
        if self.minstack:
            # 插入数据，与前一个最小值进行比较
            self.minstack.append( (x, min(x, self.minstack[-1][1]) ) )
        else:
            self.minstack.append( (x, x) )

    def pop(self):
        if self.minstack:
            self.minstack.pop()

    def top(self):
        if self.minstack:
            return self.minstack[-1][0]
        else:
            return None

    def getMin(self):
        if self.minstack:
            return self.minstack[-1][1]
        else:
            return None


class Stack_problem:

    # 1021. Remove Outermost Parentheses
    def removeOuterParentheses(self,S:str)->str:
        # 栈来存储括号，用标志符号来表示栈内存储了多少个括号
        res, flag  = [], 0
        for char in S:

            if char == "(" and flag > 0:  res.append(char)  #  无
            if char == ")" and flag > 1:  res.append(char)  # 有一个（

            if char == "(":     flag += 1
            else:               flag -= 1
        return "".join(res)

    # 1047. Remove All Adjacent Duplicates In String
    def removeDepulicates(self, S:str):
        # 栈，如果字符与栈中的字母相同则弹出栈中的字母
        res = []
        for char in S:
            if res and char == res[-1]:    # 非空重要
                res.pop()
            else:
                res.append(char)
        return "".join(res)

    # 682. Baseball Game
    def calPoints(self, ops:List[str]):

        res, number = [], 0
        for ch in ops:

            if res and ch == 'C':
                number -= res[-1]
                res.pop()
            elif res and ch == '+':
                ss = res[-1] + res[-2]
                number += ss
                res.append(ss)

            elif res and ch == 'D':
                ss = res[-1]*2
                res.append(ss)
                number += ss
            else:
                res.append(int(ch))
                number += int(ch)
        # print(res, sum(res))      #也可最后将 res， sum
        return number

    # 496. Next Greater Element I
    def nextGreaterElement(self, nums1:List, nums2:List):
        # 找到数组1中数组的下标，然后在数组2中从右开始寻找第一个比它大的数
        res = []
        for n1 in nums1:
            index = nums2.index(n1)+1
            flag = False
            for n2 in nums2[index:]:
                if n2 > n1:
                    res.append(n2)
                    flag = True
                    break
            if flag == False:
                res.append(-1)
        return res

    def nextGreaterElement_refe(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 好答案
        stack, res, dic = [], [], {}

        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                dic[stack.pop()] = nums2[i]

            stack.append(nums2[i])

        for i in range(len(nums1)):
            if nums1[i] in dic:
                res.append(dic[nums1[i]])
            else:
                res.append(-1)

        return res

    # 844. Backspace String Compare
    def backspaceCompare(self, S:str, T:str):
        def backspace(s:str):
            res = []
            for ch in s:
                if res and ch == "#":
                    res.pop()
                else:
                    if ch != "#":
                        res.append(ch)
            print(res)
            return "".join(res)
        return backspace(S) == backspace(T)

    # 20. Valid Parentheses
    def isValid(self, s: str) -> bool:
        # 用字典将括号匹配，如果匹配则栈弹出，最后栈为空则是有效括号
        res = []
        dic = {'(':')', '[':']', '{': '}'}
        left = ['(', '{', '[']
        for ch in s:
            if ch in left:
                res.append(ch)
            elif res and dic[res[-1]] == ch:
                res.pop()
            else:
                return False
        return res == []


if __name__ == '__main__':
    st = Stack_problem()
    # string = "(()())(())(()(()))"   # 1021
    # s = "abbaca"        # 1047 ->ca
    # points = ["5","2","C","D","+"]  # 682 ->30
    # S, T  = "ab#c",  "ad#c"             # 844->True
    # S1, T1 ="y#fo##f", "y#f#o##f"       # 844 ->False
    # print(st.backspaceCompare(S,T))
    mins = MinStack()
    s = "]" #20 "()[]{}" True
    n1= [1, 3, 5, 2, 4]
    n2=[6, 5, 4, 3, 2, 1, 7]
    print(st.nextGreaterElement(n1,n2))