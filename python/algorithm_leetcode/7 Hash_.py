"""https://leetcode.com/tag/hash-table/"""
from collections import Counter
from typing import List


class Hash_solution:

    # 1365. How Many Numbers Are Smaller Than the Current Number
    def smallerNumbersThanCurrent(self, nums:List[int])->List[int]:
        # 排序，将第一次出现的数字下标放入字典中存储
        n = sorted(nums)
        dic, res = {}, []
        for index, value in enumerate(n):
            if value not in dic:
                dic[value] = index
        for num in nums:
            res.append(dic[num])
        return res

    # 771. Jewels and Stones
    def numJewelsInStones(self, J:str, S:str)->int:
        count = 0
        for ch in S:
            if ch in J:
                count += 1
        return count

    # 961. N-Repeated Element in Size 2N Array
    def repeatedNTimes(self, A:List[int]):
        if not A:   return None
        dic = {}
        for i in A:
            if i in dic:    dic[i] += 1
            else:           dic[i] = 1
        for key in dic:
            if dic[key] == len(A)/2:
                return key

    # 1207. Unique Number of Occurrences
    def uniqueOccurrences(self, arr:List[int]):
        # 字典储存数字和出现的次数，键集合长度等于出现次数长度，则是独立出现的次数
        dic = {}
        for i in arr:
            if i in dic:    dic[i] += 1
            else:   dic[i]=1
        key, values = set(dic.keys()), set(dic.values())
        if len(key) == len(values): return True
        else:   return False

if __name__ == '__main__':
    hh = Hash_solution()
    # nums = [8,1,2,2,3]      # 1365  [8,1,2,2,3]  -> [4, 0, 1, 1, 3]
    # print(hh.smallerNumbersThanCurrent(nums))
    J = "aA"
    S = "aAAbbbb"       # 771
    n = [5,1,5,2,5,3,5,4]       # 961. Repeted times
    arr = [1, 2, 2, 1, 1, 3]    # 1207 True
    print(hh.uniqueOccurrences(arr))