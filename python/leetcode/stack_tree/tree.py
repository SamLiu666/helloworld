from typing import List

from leetcode.stack_tree.stack_tree import TreeNode


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # if root:
        #     return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        #
        # return []
        res, stack  = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right

    # 102. Binary Tree Level Order Traversal
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans, level = [], [root]
        while root and level:
            ans.append([node.val for node in level])
            lrpair = [(node.left, node.right) for node in level]
            level = [leaf for lr in lrpair for leaf in lr if leaf]
        return ans

    def flatten(self, root):
        self.prev = None
        if root == None:    return None
        self.flatten(root.right)
        self.flatten(root.left)

        root.right = self.prev
        root.left = None
        self.prev = root





# t = TreeNode([1,2,3,4])
# t1 = TreeNode(5)
# print(t.val, t.right, t.left, t1.val)
# dic = {}
# p = [1,3,5,11,3]
# j=0
# for i in p:
#
#     dic[j] = i
#     j = j+1
# print(dic)
# dic[1] = 5
# print(dic)