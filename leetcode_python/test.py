s = "efgabcd"
res = list(s)
count = 3
head, tail = res[0:count], res[count:]
ans = tail + head
print(ans)

count = -3
head, tail = res[0:count], res[count:]
print(tail)
ans = tail + head
print(ans)

n = [1,2,3,4]
a = n
b = list(n)
a.pop()
b.append(0)
print(a,n, b, n)

address = "1.1.1.1"
s = str(n)
ss = list(s)
l = list(address)
print(l, s,ss)