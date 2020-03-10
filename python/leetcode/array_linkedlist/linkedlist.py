class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class solution:

    def reverselist(self, head:ListNode):
        # 206翻转链表
        cur = None