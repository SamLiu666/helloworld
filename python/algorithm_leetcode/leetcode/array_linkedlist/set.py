from typing import List


def findDupicates(nums:List):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)

x = ['abb', 'baa']
print(min(x))
a = [1,3,6,2]
b = sorted(a)

print(a, b)