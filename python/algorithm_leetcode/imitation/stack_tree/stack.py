import string
from typing import List


class solution_stack:

    # p20 判断括号是否有效
    def isValid(self, s:string)->bool:
        bracket_map = {"(": ")", "[": "]", "{": "}"}
        open_par = set(["(", "[", "{"])
        stack = []
        for i in s:
            if i in open_par:
                stack.append(i)
            elif stack and i == bracket_map[stack[-1]]:
                stack.pop()
            else:
                return False
        return stack == []

s = solution_stack()
test = "()[]{}"
if '(' in test:
    print(True)
list = list(test)
list.pop()
print(list,type(list),s.isValid(test))

strs = 'abcd'
for ch in strs:
    print(ch)