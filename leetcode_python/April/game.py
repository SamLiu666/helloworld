from typing import List


class Solution:
    def minCount(self, coins: List[int]) -> int:
        l  = len(coins)
        dp = [0]*l
        for i in range(l):
            if coins[i]<=2:
                dp[i] = 1
            elif coins[i] % 2 == 1:
                dp[i] = coins[i] // 2 + 1
            else:
                dp[i] = coins[i] // 2
        count = 0
        for n in dp:
            count += n
        return count

    # 2 传递信息
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        dic = {}
        for num in relation:
            res, key, value = [], num[0], [num[1]]
            if key not in dic:
                dic[key] = value
            else:
                dic[key] += value
        # print(dic)

        visit, s, g, count = [], 0, n-1, 0
        def dfs(count):
            if s not in visit:
                visit.append(s)
                for n in dic[s]:
                    if n != g:
                        dfs(count)
                    else:
                        count += 1
        dfs(count)
        return count


if __name__ == '__main__':
    s = Solution()
    # n = [2,3,10] #[4,2,1]
    n = 5
    relation = [[0, 2], [2, 1], [3, 4], [2, 3], [1, 4], [2, 0], [0, 4]]
    k = 3
    ans = s.numWays(n, relation, k)
    # ans = s.minCount(n)
    print(ans)