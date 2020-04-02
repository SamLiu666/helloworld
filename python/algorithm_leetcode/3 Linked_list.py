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


class LinkedList_Solution:

    # 链表->列表
    def InputtoList(self, head: ListNode):
        res = []
        while head.next:
            res.append(head.val)
            head = head.next
        res.append(head.val)
        return res

    # 1290. Convert Binary Number in a Linked List to Integer
    def getDecimaValue(self, head: ListNode):
        print(head)
        value = 0
        while head:
            value = 2 * value + head.val
            head = head.next
        return value

    # 876. Middle of the Linked List
    def middleNode(self, head:ListNode):
        # 链表转换为列表，不推荐
        # A = [head]
        # while A[-1].next:
        #     print(A[-1].next)
        #     A.append(A[-1].next)
        # return A[len(A) // 2]
        # 双指针，快的是慢的两倍速
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # 876. 计数的方法
    def middleNode_fast(self, head):
        n = 1
        node = head
        while node.next != None:
            node = node.next
            n += 1
        print(self.InputtoList(node))
        if n % 2 == 0:  # even
            n = n / 2 + 1
        else:  # odd
            n = n / 2 + 0.5

        node = head
        for i in range(int(n - 1)):
            print(self.InputtoList(node))
            node = node.next
        return node

    # 206. Reverse Linked List
    def reverseList(self, head:ListNode)->ListNode:
        # 类似数组中的交换，当前指针存储好链表顺序，再逆序输出
        rervesion = None
        while head:
            current = head
            head = head.next
            current.next = rervesion
            rervesion = current
        return rervesion

    # 237. Delete Node in a Linked List
    def deleteNode(self, node):
        # 删除一个节点要知道前一个节点和后一个节点。而用改数组的方式，并不是删除节点的含义
        if node.next is None:   return
        node.val = node.next.val
        node.next = node.next.next

    # 21 Merge Two Sorted Lists
    def mergeTwoLists(self, l1:ListNode, l2:ListNode):
        if l1 is None: return l2
        if l2 is None: return l1
        if l1.val <= l2.val:    
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    # 83 Remove Dupicates from Sorted List
    def deleteDuplicates(self, head:ListNode):
        prev= head
        if head.next:
            cur = head.next

        while cur:
            if prev.val == cur.val:
                prev.next = cur.next
                cur = cur.next
            else:
                cur = cur.next
                prev = prev.next
        return head

# 列表转换为链表
def InputToListNode(nums):
    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in nums:
        ptr.next = ListNode(number)
        ptr = ptr.next
    ptr = dummyRoot.next
    # print(ptr.val)
    return ptr


if __name__ == '__main__':
    so = LinkedList_Solution()
    # a = ListNode(3)
    # print(a.val, a.next)
    # nums = InputToListNode([1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0])  # 1290  ans =18880
    nums = InputToListNode([1,1,2,3,3])       # 876.  #206 [1,2,3,4,5,6]
    # n1 = InputToListNode([1,2,4])               # 83 [1,1,2,3,3]
    # n2 =InputToListNode([1,3,4])                # 21
    n = so.deleteDuplicates(nums)
    print(so.InputtoList(n))
