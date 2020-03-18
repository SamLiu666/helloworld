from typing import List

from matplotlib import collections


class solution:

    # 哈希表解决,136
    def singleNumber(self, nums:List[int]) -> int:

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

    # Input: [0,1,0,3,12] -> Output: [1,3,12,0,0] ；操作 0 的位置
    def p2830(self, nums:List[int]):

        res = []
        n = len(nums)
        for num in nums:
            # print(num)
            if num == 0:
                temp =(nums.pop(nums.index(num)))
                # print(nums)
                res.append(temp)
        return (nums+res)

    # 不创造其他存储空间
    def p283(self, nums):
        numsOfzero = 0
        for i in nums:
            if i == 0:
                numsOfzero = numsOfzero + 1
                nums.remove(i)
                nums.append(0)
        return nums

    # 最大化元素出现次数大于N/2。Input: [2,2,1,1,1,2,2] ->Output: 2
    def p169(self, nums:List):

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

    # P448 找到数组中消失的元素
    def p449(self,nums:List):
        res = []
        for i in range(len(nums)):
            index = abs(nums[i]) -1
            nums[index]  = -abs(nums[index])

        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        return res

    # 找最短字串
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)
        start, end = -1, -1
        i=0
        while(i<len(nums)):
            if nums[i] != sortedNums[i]:
                start = i
                break
            i+=1

        if start==-1: return 0  #已经排序完成
        j = len(nums) - 1
        while j>0:
            if nums[j] != sortedNums[j]:
                end = j
                break
            j -= 1
        return end - start +1

    # 338 找出数组中1的个数，并二进制输出结果
    def countBits(self, num: int) -> List[int]:
        res = [0]
        for i in range(1, num+1):
            # >> 右移动运算符
            res.append(res[i>>1] + (i&1))
            print(res)
        return res

    # 406 给数组排队
    def reconstructQueue(self, people):
        if not people: return None

        peopledic, height, res = {}, [], []

        for i in range(len(people)):
            p = people[i]
            if p[0] in peopledic:
                peopledic[p[0]] += (p[1], i)
            else:
                peopledic[p[0]] = [(p[1], i)]
                height += p[0]

        height.sort()
        for h in height[::-1]:
            peopledic[h].sort()
            for p in peopledic[h]:
                res.insert(p[0], people[p[1]])

        return res

    def dailyTemperatures(self, T: List[int]) -> List[int]:
        pass

    def countSubstrings(self, s:str):
        L, r = len(s), 0
        for i in range(L):
            for a, b in [(i,i), (i,i+1)]:
                while a>=0 and b<L and s[a] == s[b]:
                    r += (b-a)//2
        return r

    # 238 输出除自己外数组内所有数的乘积
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        L, R, product = [0]*length, [0]*length, [0]*length
        # 计算左、右边乘积
        L[0] = 1
        for i in range(1,length):
            L[i] = nums[i-1] * L[i-1]
        print(L)
        R[length-1] = 1
        # for j in reversed(range(length-1)):
        #     R[j] = nums[j+1] * R[j+1]
        for j in range(length-1-1,-1,-1):
            R[j] = R[j+1] * nums[j+1]
        print(R)
        for i in range(length):
            product[i] = L[i] * R[i]

        return product

s=solution()
nums = [1,2,3,4]
print(s.productExceptSelf(nums))
# for j in reversed(range(5)):
#     print(j)
# for j in range(5-1, -1, -1):
#     print(j)
# a = [0,1,0,3,12]
#测试
# print(s.p283(a), s.p169(a))
# a = [1,1,2]
# s = solution()
# print(s.p136(a))
# c, b = 1, 2
# print(c,b)
# e, f = b, c
# g, h = c, b
# print(e, f)
# print(g, h)
# print(s.p449([4,3,2,7,8,2,3,1]))
# s.countBits(5)
# for i in range(3):
#     for a, b in [(i,i), (i,i+1)]:
#         print(a, b)

