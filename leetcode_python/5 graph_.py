'''https://leetcode.com/tag/graph/'''
from typing import List


class Solution:

    # 997. Find the Town Judge
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        # N个顶点的trust图，图内各点指向同一个点的次数为N-1次，用有向图的方式
        count = [0] * (N + 1)
        for i, j in trust:
            count[i] -= 1
            count[j] += 1
        for i in range(1, N + 1):
            if count[i] == N - 1:
                return i
        return -1

    # 1387. Sort Integers by The Power Value
    def getKth(self, lo: int, hi: int, k: int) -> int:
        # 应方法，按要求编码
        def pow_get(n):
            count = 0
            while n != 1:
                if n % 2 == 0:
                    n = n/2
                else:
                    n = 3*n + 1
                count += 1
            return count
        dic = {}
        for key in range(lo, hi+1):
            value = pow_get(key)
            dic[key] = value
        freq = 1
        print(dic)
        dic = sorted(dic.items(), key=lambda item:item[1])
        print(dic)
        # for key in sorted(dic.values()):
        #     if freq == k:
        #         return dic[key]
        for i in range(len(dic)):
            if i == k-1:
                return dic[i][0]

    # 959. Regions Cut By Slashes
    def regionBySlashes(self, grid:List[str])->int:
        pass


if __name__ == '__main__':
    s = Solution()
    # N = 4 #3
    # trust = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]] # 997. [[1, 3], [2, 3]]
    lo, hi, k = 12, 15, 2
    print(s.getKth(12, 15, 2))