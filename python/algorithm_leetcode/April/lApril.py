from typing import List
from collections import Counter

class solution:

    # Single Number 2020401
    def singleNumber(self, nums:List[int]):
        # #enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for i in dic:
            if dic[i] == 1:
                return i
        # nums = sorted(nums)
        # for i in range(1,len(nums)-1,2):
        #     if len(nums) % 2 == 1:
        #         return nums[-1]
        #     else:
        #         if nums[i] != nums[i-1] :
        #             return nums[i]


if __name__ == '__main__':
    s = solution()
    nums =  [2,2,1]
    print(s.singleNumber(nums))