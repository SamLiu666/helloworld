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

    # 347 大于K 次的数据
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res, frq, n = {}, {}, len(nums)
        print(n)

        for i in nums:
            if i not in res:
                res[i] = 1
            else: res[i] += 1
        print(res)

        # for key, value in res.items():
            # 返回出现K次以上的数据
            # if value>=k:
            #     print(value,key)
            #     frq.append(key)
        for z, v in res.items():
            if v not in frq:
                frq[v] = [z]
            else:
                frq[v].append(z)
        print("frq= " + str(frq))

        arr = []
        for x in range(len(nums), 0, -1):
            if x in frq:
                print(x, frq[x])
                for i in frq[x]:
                    arr.append(i)
        return arr[:k]


s = solution_hash()
nums = [ 6,1, 2,1,2,3,1,5]
n= [1]
print(s.topKFrequent(nums,1))
