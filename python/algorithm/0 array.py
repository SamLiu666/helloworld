from typing import List

"""Leetcode: https://leetcode.com/tag/array/"""

class Arrayproblem:
    """Easy 数组的题起手，记录理解过程"""

    # 1365. How Many Numbers Are Smaller Than the Current Number
    def smallerNumbersthanCurrent(self, nums:List)->List:
        # 字典+排序：排序之后的数对应的索引即为比之小的数，用哈希表存储
        dic = {}
        for index, value in enumerate(sorted(nums)):
            if value not in dic:
                dic[value] = index
        return [dic[i] for i in nums]

    # 1313. Decompress Run-Length Encoded List
    def decompressRLElist(self, nums:List):
        # 按照题意 freq, val 值表示出来，顺其自然求解
        res = []
        for i in range(0,len(nums),2):
            freq = nums[i]
            for j in range(freq):
                val = nums[i + 1]
                res.append(val)
        # 参考解法
        # result = []
        # for i in range(0, len(nums), 2):
        #     f, v = nums[i], nums[i + 1]
        #     result += [v] * f
        return res

    # 1295. Find Numbers with Even Number of Digits
    def findNumbers(self, nums:List):
        # 几位数字转换为字符串，用字符串个数奇偶去判断数据含几个的奇偶性
        count =0
        for i in nums:
            string = str(i)
            length = len(string)
            if length % 2 == 0:
                count += 1
        return count


if __name__ == '__main__':
    # 测试部分
    solution = Arrayproblem()
    # nums = [8, 1, 2, 2, 3]    #1365.[4,0,1,1,3]
    # nums = [1, 2, 3, 4]       #1313 [2,4,4,4]
    nums = [12, 345, 2, 6, 7896]  #1295 [2]
    print(solution.findNumbers(nums))