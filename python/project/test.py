a = [ 10,30,40,50,100]
b = [1,3]
for i in range(len(a)):
    print(i)
print(a+b)

for i in a:
    print(a)
    a.remove(i)
a = a + [0] * 2
print(a)