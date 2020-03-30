from typing import List


class solution:

    # 46 DFS求排列组合
    def permute(self, nums):
        res =[]
        self.dfs(nums, [], res)
        return res
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            print(res)
            # 返回之前的路径
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)

    def permute_2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.helper(nums, 0, result)
        return result
    def helper(self, nums, begin, result):
        n = len(nums)
        if begin == n:
            tmp = nums[:]
            result.append(tmp)
            return

        for i in range(begin, n):
            nums[begin], nums[i] = nums[i], nums[begin]
            self.helper(nums, begin + 1, result)
            nums[begin], nums[i] = nums[i], nums[begin]

    # 22 生成括号，回溯算法
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def back(s = '', left=0, right=0):
            if(len(s))==2*n:
                res.append(s)
                return
            if left<n:  back(s+'(', left+1, right)
            if right<left: back(s+')', left, right+1)
        back()
        return res

    # Iteratively
    def subsets(self, nums):
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res
    def dfs(self, nums, index, path, res):
        res.append(path)
        print(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i+1, path + [nums[i]], res)

    def rotate(self, A):
        A[:] = zip(*A[::-1])
        return A

s = solution()
nums = [1,2,3]
n = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
# print(s.permute_2(nums), s.generateParenthesis(3), sep='\n')
print(s.rotate(n))