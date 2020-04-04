"""https://leetcode.com/tag/tree/"""

class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def StringtoInt(input):
    return int(input)

def InttoString(input):
    if input is None:   input = 0
    return str(input)

def ListToTree(nums):
    pass