def permute(nums):
    def backtrack(first=0):
        # 所有数都填完了
        if first == n:
            res.append(nums[:])

        for i in range(first, n):
            # 动态数组维护
            nums[first], nums[i] = nums[i], nums[first]
            # 继续递归下一个数
            backtrack(first+1)
            # 回退，撤销操作
            nums[first], nums[i] = nums[i], nums[first]

    n = len(nums)  # n 判断条件
    res = []   # output
    backtrack()
    return res

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, size, depth, path, used, res):
            if depth == size:
                res.append(path[:])
                return

            for i in range(size):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])

                    dfs(nums, size, depth + 1, path, used, res)

                    # 回退，撤销操作
                    used[i] = False
                    path.pop()

        size = len(nums)
        if len(nums) == 0:
            return []

        used = [False for _ in range(size)]
        res = []
        dfs(nums, size, 0, [], used, res)
        return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    solution = Solution()
    res = solution.permute(nums)
    print(res)
