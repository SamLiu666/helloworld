"""https://leetcode.com/tag/tree/"""
from typing import List


class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

def StringtoInt(input):
    return int(input)

def InttoString(input):
    if input is None:
        input = 0
    return str(input)

def StringToTree(input):
    """字符串->列表->树
    返回，树，打印树的结构"""
    # 去除字符串空格
    input = input.strip()
    input = input[0:]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    res = []
    root = TreeNode(int(inputValues[0]))
    res.append(root.val)
    nodeQueue = [root]
    front = 0
    index = 1

    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

            res.append(node.left.val)
        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)

            res.append(node.right.val)
    print(res, type(nodeQueue), len(nodeQueue))
    return root

# 待完善
def ListToTree(input:List):
    res = []    # 存放输入的树的结构
    root = TreeNode(input[0])
    res.append(root.val)
    front, index, nodeQueue  = 0, 1, [root]
    
    while index < len(input):
        node = nodeQueue[front]
        front += 1
        
        item = input[index]
        index += 1  
        if item != None:
            leftNumber = item
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)
            
            res.append(node.left.val)
        
        if index >= len(input):
            break
            
        item = input[index]
        index += 1
        if item != None:
            rightNumber = item
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
            res.append(node.right.val)
        
    print(res, len(nodeQueue))
    return root


def treeNodeToString(root:TreeNode):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    print("[" + output[:] + "]")
    return "[" + output[:] + "]"

class Tree_Solution:

    # 938. Range Sum of BST
    def rangeSumBST(self, root:TreeNode,L,R):
        # DFS 如果在路劲之内则相加，二叉树搜索
        def dfs(node):
            if node:
                if L <= node.val <= R:
                    self.ans += node.val
                if L < node.val:
                    dfs(node.left)
                if node.val < R:
                    dfs(node.right)

        self.ans = 0
        dfs(root)
        return self.ans


    # 617 Merge two binary tree
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        # 左边 = 两个树的左边， 右边= 两个数的右边
        if t1 is None:  return t2
        if t2 is None:  return t1
        t1.val = t1.val + t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1

    # 589 N-ary Tree Preorder Traversal
    def preorder(self, root:Node):
        child_nodes = []

        if root != None:
            child_nodes.append(root.val)

            for node in root.children:
                child_nodes += self.preorder(node)

        return child_nodes

    # 700. Search in a Binary Search Tree
    def searchBST(self, root: object, val: object) -> object:
        # 二叉树特性，左边比节点小， 右边比节点大
        if not root:            return None
        if root.val == val:     return root
        elif val<root.val :     return self.searchBST(root.left, val)
        else:                   return self.searchBST(root.right, val)

    # 897. Increasing Order Search Tree
    def increasingBST(self, root: TreeNode) -> TreeNode:
        # 左边节点加入右边，切掉左边
        def inorder(root:TreeNode):
            if root:
                inorder(root.left)
                root.left = None
                self.current.right = root
                self.current = root
                inorder(root.right)
        ans = self.current = TreeNode(None)
        inorder(root)
        return ans.right

if __name__ == '__main__':
    t =Tree_Solution()
    # input = '10,5,15,3,7,null,18'  # 938 ->32
    # t1, t2 = '1,3,2,5' , '2,1,3,null , 4,null , 7'
    # n1 = StringToTree(t1)
    # n2 = StringToTree(t2) # 617
    # 700  '4,2,7,1,3' , 2 -> '2,7,1'
    # 897 '5,3,6,2,4,null,8,1,null,null,null,7,9'
    n = '5,3,6,2,4,null,8,1,null,null,null,7,9'
    n = StringToTree(n)
    ans = t.increasingBST(n)
    # ans = t.searchBST(n, 2)
    # print(type(ans))
    treeNodeToString(ans)


    # print(t.rangeSumBST(nums, 7, 15) )
    # print(t.rangeSumBST(n2, 7, 15) )