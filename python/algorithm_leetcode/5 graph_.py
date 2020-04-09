'''https://leetcode.com/tag/graph/'''
from typing import List


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        dic = {}
        for i in trust:
            dic[i[0]] = i[1]
        s = set(dic.values())
        if len(s) == 1: return s.pop()
        else: return -1


if __name__ == '__main__':
    s = Solution()
    N = 4 #3
    trust = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]] #[[1, 3], [2, 3]]

    print(s.findJudge(N,trust))
