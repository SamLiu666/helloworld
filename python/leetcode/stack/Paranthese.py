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


s = solution()
stest = "(())())"
print(s.pro_1021(stest), s.pro1021_1(stest))