class Solution:

    def reformat(self, s: str) -> str:
        num1, alp = [], []
        for ch in s:
            if ch.isdigit():
                num1.append(ch)
            if ch.isalpha():
                alp.append(ch)
        if len(num1) == len(s) or len(alp) == len(s):
            return ""
        l1, l2, res = len(num1), len(alp), []
        # distance = abs(l1-l2)
        if l1-l2==1:
            for i in range(l2):
                res.append(num1[i])
                res.append(alp[i])
            res.append(num1[-1])
        else:
            for i in range(l2):
                res.append(alp[i])
                res.append(num1[i])
            res.append(alp[-1])
        return "".join(res)
