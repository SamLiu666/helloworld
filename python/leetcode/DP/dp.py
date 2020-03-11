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