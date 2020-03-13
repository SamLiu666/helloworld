class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class solution:
    # 206翻转链表
    def reverselist(self, head:ListNode):
        cur = None

    # P21 合并两个链表，递归
    def mergeTwoLists(self, l1, l2):
        if l1 == None: return l2
        if l2 == None: return l1
        if(l1.val < l2.val):
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    # p 141 链表循环
    def hasCycle(self, head:ListNode)->bool:
        # try:
        #     slow = head
        #     fast = head.next
        #     while slow is not fast:
        #         slow = slow.next
        #         fast = fast.next.next
        #     return True
        # except:
        #     return False
        # 双指针解法，快指针慢指针
        slow = head
        fast = head.next
        while(slow!=fast):
            if(fast == None or fast.next == None): return False
            slow = slow.next
            fast = fast.next.next
        return True