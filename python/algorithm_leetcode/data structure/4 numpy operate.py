import numpy as np

print('*** basic ***')
a = np.array([2,3,4])
b = np.arange(1,10,1)
c = b.reshape(3,3)      # 变换矩阵的格式为 三行三列
d = np.linspace(1, 10, 4)    # 均匀分布
print(a, b, c, d, d.size # 矩阵内所含多少元素
      , sep='\n' )

print('*** m*n array ***')
e = np.array([(1,1,1), (2,2,2), (3,3,3)])
f = e * 2
g = np.zeros((3,3))     # 0 矩阵
h = np.ones((3,3))
i = np.random.random((3,3))     # 随机足证0 -1
result = i.sum()
print(c < 5, e, f, g, h, i, result, sep='\n')

