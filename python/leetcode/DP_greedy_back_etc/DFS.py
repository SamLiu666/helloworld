import collections
from collections import defaultdict


class dfs_solution:

    # 39. Combination Sum
    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        # print(res)
        return res

    def dfs(self,nums, target, index, path, res):
        if target < 0:
            return # backtarcking
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            self.dfs(nums, target - nums[i], i, path + [nums[i]], res )
            print(res)

    # 49. Group Anagrams
    def groupAngrams(self, strs):
        answer = defaultdict(list)
        for s in strs:
            answer[tuple(sorted(s))].append(s)
            # answer[sorted(s)].append(i)
            print(answer)
        return answer.values()

    def groupAnagrams_1(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()

    def group(self, strs):
        d = {}
        for s in strs:
            sorts = ''.join(sorted(s))
            if sorts in d:
                temp = d[sorts]
                temp.append(s)
                d[sorts] = temp
            else:
                d[sorts] = [s]
        return d.values()

s = dfs_solution()
# nums = [2,3,6,7]
# result = s.combinationSum(nums, 7)
# print(s.combinationSum(nums, 7))
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# print("s =",  s.groupAngrams(strs))
print(s.groupAnagrams_1(strs), s.group(strs), sep='\n')
# s = "szcsa"
# sorts = ''.join(sorted(s))
# print(type(sorts),s,sorts)