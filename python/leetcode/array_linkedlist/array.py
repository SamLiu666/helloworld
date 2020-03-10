from typing import List

from matplotlib import collections


class solution:

    def singleNumber(self, nums:List[int]) -> int:
        # 哈希表解决,136
        hash_table = []
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0]

    def p136(self, nums):
        res = []
        for i in nums:
            if i not in res:
                res.append(i)
            else: res.remove(i) #移除列表中第一个匹配项
        return res.pop()

    def p2830(self, nums:List[int]):
        # Input: [0,1,0,3,12] -> Output: [1,3,12,0,0] ；操作 0 的位置
        res = []
        n = len(nums)
        for num in nums:
            # print(num)
            if num == 0:
                temp =(nums.pop(nums.index(num)))
                # print(nums)
                res.append(temp)
        return (nums+res)

    def p283(self, nums):
        # 不创造其他存储空间
        numsOfzero = 0
        for i in nums:
            if i == 0:
                numsOfzero = numsOfzero + 1
                nums.remove(i)
                nums.append(0)
        return nums

    def p169(self, nums:List):
        # 最大化元素出现次数大于N/2。Input: [2,2,1,1,1,2,2] ->Output: 2
        # 用哈希表的方式解决,collection 库
        # counts = collections.Counter(nums)
        # return max(counts.keys(), key=counts.get)
        # 排序算法，最大值在数据中间
        # nums.sort()
        # return nums[len(nums)//2]
        #投票法
        count, candidate = 0, None
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num==candidate else -1
        return candidate


s=solution()
a = [0,1,0,3,12]
print(s.p283(a), s.p169(a))

# a = [1,1,2]
# s = solution()
# print(s.p136(a))
#
# c, b = 1, 2
# e, f = b, c
# g, h = c, b
# print(e, f)
# print(g, h)

