# Node for Linked List https://leetcode.com/problems/design-linked-list/
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class linked_list:

    def __init__(self):
        self.head = None
        self.size = 0   # size of linklist

    def get(self, index:int)->int:
        """Get the value of the index-node in the linked list. if the index is valid return -1"""
        if self.head is None or index >= self.size or index < 0:
            return -1
        count, pre = 0, self.head
        # while count < index-1:
        #      pre = pre.next
        #      count += 1
        for i in range(index):
            pre = pre.next
        return pre.data

    # add data in the front
    def addAtHead(self, val: int) -> None:
        """Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list."""
        node = Node(val)
        node.next = self.head
        self.head = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        cur, node = self.head, Node(val)
        if self.head is None:
            self.head = node
        else:
            while cur.next:
                cur = cur.next
            cur.next = node
        print("add ", node.data)
        self.size += 1

    def addAtIndex(self, index, val):
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)

        else:
            cur = self.head
            for i in range(index-1):
                cur = cur.next
            node = Node(val)
            node.next = cur.next
            cur.next = node
            self.size += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return

        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return

        cur = self.head
        for i in range(1, index):
            cur = cur.next
        cur.next = cur.next.next
        self.size -= 1

    # link list Traverlsal
    def showList(self):
        # use array to store
        res = []
        pre = self.head
        while pre:
            res.append(pre.data)
            self.size += 1
            pre= pre.next
        print(res)
        return res


class linked_list_2:

    def __init__(self):
        self.head = None
        self.size = 0  # size of linklist

    # empty size?
    def isEmpty(self):
        if self.size == 0:
            print("LinkList is Empty")
            return True
        else:
            print("LinkList is not Empty")
            return False

    # link list Traverlsal
    def showList(self):
        # use array to store
        res = []
        pre = self.head
        while pre:
            res.append(pre.data)
            pre = pre.next
        print(res)
        return res


# Using list to design linked list is also a good way.
class linked_list_3:
    # use list
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.linkedlist = list()

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= len(self.linkedlist):
            return -1
        else:
            return self.linkedlist[index]

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        self.linkedlist.insert(0, val)

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        self.linkedlist.append(val)

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if 0 <= index and index <= len(self.linkedlist):
            self.linkedlist.insert(index, val)

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if 0 <= index and index < len(self.linkedlist):
            self.linkedlist.pop(index)


if __name__ == '__main__':

    # first method to create linked list
    l2 = linked_list_2()

    # use the attribute to add node
    l2.head = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    l2.head.next = node2
    node2.next = node3
    l2.showList()   # [1, 2, 3]


    link = linked_list()
    # addhead
    link.addAtHead(3)
    link.addAtHead(2)
    link.addAtHead(1)
    link.addAtTail(4)
    link.showList()
    # [1, 2, 3, 4]

    link.addAtIndex(2,6)     # [1, 2, 6, 3, 4]
    link.showList()
    link.deleteAtIndex(2)   # [1, 2, 3, 4]
    print(link.size)
    link.showList()
    # link.isEmpty()
    print(link.get(3))
