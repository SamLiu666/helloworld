Similar to the array, the linked list is also a `linear` data structure.

- Understand the structure of singly linked list and doubly linked list;

- Implement traversal, insertion, deletion in a singly or doubly linked list;

- Analyze the complexity of different operations in a singly or doubly linked list;

- Use two-pointer technique (fast-pointer-slow-pointer technique) in the linked list;

- Solve classic problems such as reverse a linked list;

- Analyze the complexity of the algorithms you designed;

- Accumulate experience in designing and debugging.

  Add O(1) 		Delete  O(n)

![image-20200303095600904](C:\Users\liu\AppData\Roaming\Typora\typora-user-images\image-20200303095600904.png)

It takes us `O(N)` time on average to `visit an element by index`, where N is the length of the linked list.

![image-20200303100322352](C:\Users\liu\AppData\Roaming\Typora\typora-user-images\image-20200303100322352.png)

![image-20200303100353664](C:\Users\liu\AppData\Roaming\Typora\typora-user-images\image-20200303100353664.png)

![image-20200303100412664](C:\Users\liu\AppData\Roaming\Typora\typora-user-images\image-20200303100412664.png)

Two-Pointer in Linked List.

1. `If there is no cycle, the fast pointer will stop at the end of the linked list.`
2. `If there is a cycle, the fast pointer will eventually meet with the slow pointer.`

It is a safe choice to move the slow pointer `one step` at a time while moving the fast pointer `two steps` at a time. For each iteration, the fast pointer will move one extra step. If the length of the cycle is M, after M iterations, the fast pointer will definitely move one more cycle and catch up with the slow pointer.



Summary - Two-Pointer in Linked List

If we want to insert a new node `cur` after an existing node `prev`, we can divide this process into two steps:

1. link `cur` with `prev` and `next`, where `next` is the original next node of `prev`;![img](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/28/screen-shot-2018-04-28-at-173045.png)
2. re-link the `prev` and `next` with `cur`. ![img](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/29/screen-shot-2018-04-28-at-173055.png)

Similar to the singly linked list, both the time and the space complexity of the add operation are `O(1)`.

## Summary - Linked List

------

### Review

------

Let's briefly review the performance of the singly linked list and doubly linked list.

They are similar in many operations:

1. Both of them are `not able to access the data at a random position` in constant time.
2. Both of them are able to `add a new node after given node or at the beginning of the list in O(1) time`.
3. Both of them are able to `delete the first node in O(1) time`.

But it is a little different to `delete a given node` (including the last node).

- In a singly linked list, it is not able to get the previous node of a given node so we have to spend `O(N)` time to find out the previous node before deleting the given node.
- In a doubly linked list, it will be much easier because we can get the previous node with the "prev" reference field. So we can delete a given node in `O(1)` time.

![image-20200303114826463](C:\Users\liu\AppData\Roaming\Typora\typora-user-images\image-20200303114826463.png)