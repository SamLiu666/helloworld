"""列表操作"""
# a = [ 10,30,40,50,100]
# b = [1,3]
# for i in range(len(a)):
#     print(i)
# print(a+b)
#
# for i in a:
#     print(a)
#     a.remove(i)
# a = a + [0] * 2
# print(a)
"""字典操作"""
# res = {}
# n = 4
# for i in range(n):
#     res[i] = i+2
#     print(res[i])
# print(res)
# dic = {1:1, 2:2, 1:3}
# for i,j in enumerate(dic):
#     print(i, j)

nums = [ 10,30,40,50,100]
for i, loot in enumerate(nums[1:],start=2):
    print(i, loot, type(nums))