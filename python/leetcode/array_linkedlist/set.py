from typing import List


def findDupicates(nums:List):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)

