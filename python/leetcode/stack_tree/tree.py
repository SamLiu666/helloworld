class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# t = TreeNode([1,2,3,4])
# t1 = TreeNode(5)
# print(t.val, t.right, t.left, t1.val)
dic = {}
p = [1,3,5,11,3]
j=0
for i in p:

    dic[j] = i
    j = j+1
print(dic)
dic[1] = 5
print(dic)