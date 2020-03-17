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

# last now
# 0 0
# 0 1
# 0 1
# 1 2
# 1 2
# 2 4
# 2 4
# 4 4

# 0 0
# 1 1
# 1 1
# 3 3
# 3 3
# 6 6
# 6 6
# 7 7