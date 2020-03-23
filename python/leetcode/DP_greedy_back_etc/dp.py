from typing import List


class solution:

    # p121 最好买卖股票时机，DP/Greedy
    def maxprofit(self, prices:List[int]):
        if len(prices) == 0: return 0
        n = len(prices)
        profit = 0
        minprice = prices[0]

        for i in range(n):
            if prices[i] > minprice:
                profit = max(profit, prices[i] - minprice)
            else:
                minprice = prices[i]
        return profit

    # p70   爬梯子，动态规划
    def climbstais(self, n:int):
        if n==1: return 1

        dp = [1,1]
        for i in range(2,n+1):
            dp.append(dp[i-1] + dp[i-2])
        return dp[n]

    # p 53 字串最大和
    def maxSuAbbray(self, nums:List[int]):
        if not nums: return 0
        cursum, maxsum = nums[0], nums[0]
        for num in nums[1:]:
            cursum = max(num, cursum + num)
            maxsum = max(maxsum, cursum)
        return maxsum

    # p 198 利润最大化
    def robhouse(self, nums:List):
        #  运行时间过长
        # def robwho(nums, n):
        #     if n<0: return 0
        #     return max(robwho(nums, n-1), robwho(nums, n-2) + nums[n])
        # return robwho(nums, len(nums) -1)
        last, now = 0, 0
        for i in nums:
            temp = last
            last = now
            now = max(temp + i, now)
        # last, now = now, max(last + i, now)   # 一行实现
        return now

    # 62. Unique Paths
    def uniquePaths1(self, m, n):
        # DP
        dp = [[1]*m for i in range(n)]

        for i in range(1,n):
            for j in range(1, m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

    #64. Minimum Path Sum
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [0] * n
        for i in range(m):
            dp[0] += grid[i][0]
            for j in range(1, n):
                dp[j] = (min(dp[j], dp[j-1]) + grid[i][j])
        return dp[-1]

    #
    def numTree(self, n):
        res = [0] * (n+1)
        res[0] = 1
        for i in range(1, n+1):
            for j in range(1, i):
                res[i] += res[j] * res[i-1-j]
        return res[n]


grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
m = len(grid)
n = len(grid[0])
print(m,n)