"""stack: https://leetcode.com/tag/stack/"""

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


if __name__ == '__main__':
    st = Stack_problem()
    string = "(()())(())(()(()))"
    print(st.removeOuterParentheses(string))
