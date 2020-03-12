class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

t = TreeNode([1,2,3,4])
t1 = TreeNode(5)
print(t.val, t.right, t.left, t1.val)