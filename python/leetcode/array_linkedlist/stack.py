class solution:

    def decodeString(self, s:str):
        stack, i = [], 0
        while i<len(s):
            if s[i].isdigit():
                num = ""
                while s[i] != '[':
                    num = num + s[i]
                    i += 1
                stack.append(num)

            elif s[i].isalpha() or s[i] == "[":
                stack.append(s[i])
                i += 1

            # s[i] == ']'
            else:
                pop = ""
                while stack[-1] != '[':
                    pop = stack.pop() + pop
                stack.pop()
                k = int(stack.pop())
                res = ""
                for j in range(k):
                    res = res + pop
                stack.append(res)
                i += 1

        while stack:    "".join(stack)

a= [1,[2,3,4]]
z,x,c = a.pop()
print(z,x,c)