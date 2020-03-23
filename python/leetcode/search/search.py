import math


class solution:
    pass


m=  7
n = 3
# print(math.factorial(m + n - 2) / (math.factorial(n - 1) * math.factorial(m - 1)))  # 阶乘
dp = [[1]*m for i in range(n)]
print(dp)