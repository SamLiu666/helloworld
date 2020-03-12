from typing import List


class solution_hash:

    # p 1 两数之和等于给定的目标
    def twoSum(self, nums: List, target: int):
        #用字典作为哈希表来做
        res = {}
        for i, n in enumerate(nums):
            if n in res:
                return [res[n], i]
            res[target-n] = i

