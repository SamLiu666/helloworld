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

    # 1389. Create Target Array in the Given Order
    def createTargetArray(self, nums:List, index:List):
        # 可以用zip（nums,index）
        res = []
        for i in range(len(nums)):
            res.insert(index[i], nums[i])
        return res

    # 1266. Minimum Time Visiting All Points
    def minTimeToVisitAllPoints(self, points:List[List]) -> int:
        # 每次只能移动一个单位，因此最终的距离即为两者之间的最大值
        l, count = len(points), 0
        for i in range(l-1):
            p1, p2 = points[i], points[i+1]
            # 每次只能移动一格
            dis_x = abs(p1[0]-p2[0])  # 两点 x 坐标的距离
            dis_y = abs(p1[1]-p2[1])  # 两点 y 坐标的距离
            count += max(dis_x, dis_y)
        return count

    # 1299. Replace Elements with Greatest Element on Right Side
    def replaceElements(self, arr:List):
        # 从指定位置切片，引入数组；也可原地变换
        length = len(arr)
        target = []*length
        for i in range(length):
            if arr[i+1:] == []:
                target.append(-1)
            else:
                res = max(arr[i+1:])
                target.append(res)
        return target

    # 1351. Count Negative Numbers in a Sorted Matrix
    def countNegatives(self, grid):
        # 数小于零的数
        count = 0
        for i in grid:
            for j in i:
                if j <0:
                    count += 1
        return count


if __name__ == '__main__':
    # 测试部分
    solution = Arrayproblem()
    # 题目测试集
    # nums = [8, 1, 2, 2, 3]    #1365.[4,0,1,1,3]
    # nums = [1, 2, 3, 4]       #1313 [2,4,4,4]
    #nums = [12, 345, 2, 6, 7896]  #1295 [2]
    # nums = [0, 1, 2, 3, 4]
    # index = [0, 1, 2, 2, 1]     #1389 [0,4,1,3,2]
    # points = [[1, 1], [3, 4], [-1, 0]]   # 1266: 7
    arr = [17, 18, 5, 4, 6, 1]  # 1299
    grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]  # 1351 -> 8
    print(solution.countNegatives(grid))