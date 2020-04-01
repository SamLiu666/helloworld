"""https://leetcode.com/tag/linked-list/"""


# # Definition for singly-linked list.
# 定义链表
# class LinkedList:
#
#     def __init__(self):
#         self.head_, self.tail_ = None, None
#
#     def isEmpty(self):
#         return self.head_ is None
#
#     def append(self, value):
#         # 添加元素到链表最后
#         node = ListNode(value)
#         if self.isEmpty():
#             self.head_ = node
#             self.tail_ = node
#         else:
#             self.head_.next = node
#             self.tail_ = node
#
#     def iter(self):
#         # 链表的显示
#         if self.isEmpty():  return "Empty"
#         res = []
#         current = self.head_
#         # print(current.val)
#         res.append(str(current.val)+ ' -> ')
#         # yield current.val
#         while current.next:
#             current = current.next
#             # print(current.val, " ")
#             res.append(str(current.val) + ' -> ')
#             # yield current.val
#         print( "".join(res))

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def InputToListNode(nums):
    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in nums:
        ptr.next = ListNode(number)
        ptr = ptr.next
    ptr = dummyRoot.next
    return ptr


class LinkedList_Solution:

    #1290. Convert Binary Number in a Linked List to Integer
    def getDecimaValue(self, head:ListNode):
        print(head)
        value = 0
        while head:
            value = 2*value + head.val
            head = head.next
        return value


if __name__ == '__main__':
    so = LinkedList_Solution()
    # a = ListNode(3)
    # print(a.val, a.next)
    num =  InputToListNode([1,0,1])
    print(so.getDecimaValue(num))


