"""https://leetcode.com/tag/tree/"""
from typing import List


class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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
        
class Tree_Solution:

    # 938. Range Sum of BST
    def rangeSumBST(self, root:TreeNode,L,R):
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


if __name__ == '__main__':
    input = '10,5,15,3,7,null,18'
    root = [10,5,15,3,7, None ,18]
    # nums = StringToTree(input)
    n2 = ListToTree(root)
    t =Tree_Solution()

    # print(t.rangeSumBST(nums, 7, 15) )
    # print(t.rangeSumBST(n2, 7, 15) )