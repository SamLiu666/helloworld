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