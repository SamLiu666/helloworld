from collections import defaultdict, Counter

squares = []
for x in range(10):
    squares.append(x**2)
# map() 会根据提供的函数对指定序列做映射。
squares_1 = list(map(lambda  x: x**2, range(10)))
squares_2 = [x**2 for x in range(10)]

another = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(another)
default = defaultdict(dict)
for i, j in another:
    default[i] = j
print(default)
c = Counter(default)
print(c)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print([[row[i] for row in matrix] for i in range(4)])

aa = [[] for i in range(4)]
print(aa)