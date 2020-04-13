'''https://leetcode.com/tag/heap/'''
import heapq
from typing import List


class Solution:

    # 1046 Last Stone Weight
    def lastStoneWeight(self, stones: List[int]) -> int:
        pass


"""heap is the data structure that the parent node is small than the children nodes"""
h = [3,1,5,9,4,8,6]
print(h)
heapq.heapify(h)
print(h)
heapq.heappop(h)
print(h)
heapq.heappush(h,7)
print(h)