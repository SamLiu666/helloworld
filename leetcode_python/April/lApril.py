import heapq
from typing import List
from collections import Counter

"""2020 04 mouth leetcode program"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 4/10
class MinStack:

    def  __init__(self):
        self.res = []

    def push(self, x):
        if not self.res:
            self.res.append( (x,x) )
        else:
            self.res.append( (x, min(x, self.res[-1][1])))

    def pop(self):
        if self.res:
            self.res.pop()
        else:
            return None

    def top(self):
        if self.res:
            return self.res[-1][0]

    def getMin(self):
        if self.res:
            return self.res[-1][1]


# 4/1 -- 4/14
class solution:

    # 4/ 1Single Number
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

    # 4/2  Happy Number
    def isHappy(self, n: int) -> bool:
        def standard(n):
            res, count = [], 0
            while n !=0:
                b = n%10
                res.append(b)
                n = n//10
            for i in res:
                count += i**2
            return count
        m = set()
        while n != 1:
            n = standard(n)
            if n in  m: return False
            else:       m.add(n)
        return True

    # 4/2
    def ishappy(self, n:int):
        all_number = set()
        while n !=1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in all_number:
                return False
            else:
                all_number.add(n)
        return True

    # 4/3
    def maxSubArray(self, nums: List[int]) -> int:
        # DP，找到当前最大值，全部最大值取当前最大值和之前最大值的最大值~
        if not nums: return 0
        cursum, maxsum = nums[0], nums[0]
        for num in nums[1:]:
            cursum = max(num, cursum + num)
            maxsum = max(maxsum, cursum)
        return maxsum

    # 4/4
    def moveZeroes(self, nums:List[int]):
        for i in nums:
            if i == 0:
                nums.remove(i)
                nums.append(0)
        return nums

    # 4/5
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)-1):
            cur = prices[i+1] - prices[i]
            if cur >0:
                profit += cur
        return profit

    # 4/6
    def groupAnagrams(self, strs:List[str]):
        if not strs:    return None
        dic = {}
        for s in strs:
            ch = "".join(sorted(s))
            if ch in dic:    dic[ch] += [s]
            else:           dic[ch] = [s]
        return dic.values()

    # 4/7
    def countElements(self, arr: List[int]) -> int:
        count, dic = 0, {}
        for i in arr:
            if i in dic:    dic[i] += 1
            else:           dic[i] = 1
        arr1 = set(arr)
        for i in arr1:
            if i+1 in dic:
                count += dic[i]
        return count

    # 4/8
    def middleNode(self, head: ListNode) -> ListNode:
        fast =  low = head
        while fast and fast.next:
            low = low.next
            fast = fast.next.next
        return low

    # 4/9
    def backspaceCompare(self, S: str, T: str) -> bool:
        def handle(s:str, res):
            if not s: return ""
            for ch in s:
                if res and ch == '#':   res.pop()
                if ch != '#':           res.append(ch)
            return "".join(res)
        res1, res2 = [], []
        res1 = handle(S, res1)
        res2 = handle(T, res2)
        print(res1,res2)
        return res1 == res2

    # 4/10
    # 4/11
    def diameterOfBinaryTree(self, root) -> int:
        # DFS search return the depth sum of left tree and right tree
        self.ans = 1
        def depth(node):
            if not node: return 0
            L = depth(node.left)
            R = depth(node.right)
            self.ans = max(self.ans, L+R+1)
            return max(L, R) + 1

        depth(root)
        return self.ans - 1

    # 4/12
    def lastStoneWeight(self, stones: List[int]) -> int:
        # for i in range(len(stones) - 1):
        #     stones.sort()
        #     stones.append(stones.pop() - stones.pop())
        # return stones[0]
        h = [-x for x in stones]
        heapq.heapify(h)
        while len(h) > 1 and h[0] != 0:
            heapq.heappush(h, heapq.heappop(h)-heapq.heappop(h))
        return -h[0]

    # 4/13
    def findMaxLength(self, nums: List[int]) -> int:
        # use hashmap
        dic, count, maxlen = {}, 0, 0
        dic[0] = 0
        for index, n in enumerate(nums, 1):
            if n == 0:
                count -= 1
            else:
                count += 1

            if count in dic:
                maxlen = max(maxlen, index-dic[count])
            else:
                dic[count] = index
        return maxlen

    # 4/14
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        # 符合题意写出限制
        count, res, length = 0, list(s), len(s)
        for n in shift:
            if n[0] == 0:
                count += n[1]
            else:
                count -= n[1]

        count %= length  # 改变大于长度的情况，同时，往右则取余从负为正，可直接输出
        print(count)
        return s[count:] + s[:count]
        # head, tail = res[0:count], res[count:]
        # ans = tail+head
        # return "".join(ans)


# 4/15 --
class solution_3:

    # 4/15 Product of Array Except Self
    def productExceptSelf_1(self, nums: List[int]) -> List[int]:
        # 方法一，每次计算，每次存储，超时
        def product(nums, n):

            res = list(nums)  # 新建一个对象，防止改变原有的数组
            ans = 1
            res.remove(n)
            for i in res:
                ans *= i
            return ans
        res = []
        for n in nums:
            res.append(product(nums, n))
        print(nums)
        return res

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 对应的左边乘积*右边
        length = len(nums)
        l_product, r_product = [1]*length, [1]*length

        # 左边乘积
        for i in range(1,length):
            l_product[i] = l_product[i-1] * nums[i-1]
        print(l_product)

        # 右边乘积
        start = length-1-1
        for i in range(start,-1, -1):
            r_product[i] = r_product[i+1] * nums[i+1]
        print(r_product)

        # 总乘积
        pro = []
        for i in range(length):
            ans = r_product[i] * l_product[i]
            pro.append(ans)
        return pro

    # 4/16 Valid Parenthesis String
    def checkValidString(self, s: str) -> bool:

        l = r = 0
        for ch in s:
            if ch == "(":
                l += 1
            else:
                l -= 1
            if ch != ")":
                r += 1
            else:
                r -= 1
            if r<0:
                break
            l = max(l, 0)
        return l == 0

    def check_2(self, s):
        # do not work for left must before right
        l, r, star = s.count("("), s.count(")"), s.count("*")
        lr = l-r
        if lr == 0:
            return True
        else:
            return abs(l-r) == star

    # 4/17 Number of Islands
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, i, j):
            if i<0 or j<0 or i>len(grid) or j >len(grid[0]) or grid[i][j] != "1":
                return
            grid[i][j] = '#'
            dfs(grid, i+1, j)
            dfs(grid, i-1, j)
            dfs(grid, i, j+1)
            dfs(grid, i, j-1)

        if not grid:    return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    count += 1
        return count

    # 4/18
    def minPathSum(self, grid: List[List[int]]) -> int:
        col, row = len(grid), len(grid[0])
        for i in range(col):
            for j in range(row):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[i][j] += grid[i][j - 1]
                elif j == 0:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] += min(grid[i][j - 1], grid[i - 1][j])
        return grid[-1][-1]


if __name__ == '__main__':
    # s = solution()
    # nums =  [2,2,1]
    # n = 19
    # nums = [0,1,0,3,12]
    # print(s.isHappy(n),  s.ishappy(n))
    # print(s.moveZeroes(nums))
    # nums = [-2,1,-3,4,-1,2,1,-5,4]
    # nums = [7,1,5,3,6,4]
    # nums2 = [1,2,3,4,5]
    # strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    # print(s.groupAnagrams(strs))
    # arr = [1, 1, 3, 3, 5, 5, 7, 7]
    # S = "y#fo##f"
    # T = "y#f#o##f"
    # ans = s.backspaceCompare(S,T)
    # print(ans)
    # obj = MinStack()
    # obj.push(3)
    # obj.push(2)
    # obj.push(-1)
    # # obj.pop()
    # param_3 = obj.top()
    # param_4 = obj.getMin()
    # print(param_3,param_4)
    # n = [0, 0, 1, 0, 0, 0, 1, 1]    # 6
    # ans = s.findMaxLength(n)
    # so = "abcdefg"
    # shift = [[1, 1], [1, 1], [0, 2], [1, 3]]
    # ans1 = s.stringShift(so, shift)
    #
    # ss = "xqgwkiqpif"
    # shift1 = [[1,4],[0,7],[0,8],[0,7],[0,6],[1,3],[0,1],[1,7],[0,5],[0,6]]
    # ans = s.stringShift(ss,shift1)
    # print(ans)
    # # print(ans1)
    s_3 = solution_3()
    # n = [1,2,3,4]   # 4/15
    # ans = s_3.productExceptSelf(n)
    # n = "((*))))" #"(*))"  # 4/16
    # grid = [["1","1","1","1","0"],["1","1","0","1","0"],
    #         ["1","1","0","0","0"],["0","0","0","0","0"]]
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    ans = s_3.minPathSum(grid)
    print(ans)
