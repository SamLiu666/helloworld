# 导览

## 基础
数据结构的存储方式主要分为：数组（顺序存储）、链表（链式存储）

数组：连续存储，随机访问，通过索引寻找对应位置，节约存储空间。扩容要重新分配内存，插入和删除都需要移动后面的数据，时间复杂度为 O(N)。

链表：元素不连续，指针指向下一个元素的位置，不存在数组的扩容为题，不能随机访问。插入或删除元素，时间复杂度为O(1)。



## 基本操作

遍历、访问、增加、删除、查找、修改

各种数据结构的遍历 + 访问无非两种形式：线性的和非线性的。

线性就是 for/while 迭代为代表，非线性就是递归（在函数定义中使用函数自身的方法）为代表。[迭代与递归](https://www.jianshu.com/p/32bcc45efd32)

```Java
void traverse(int[] arr) {
    //数组遍历框架，线性迭代结构
    for (int i = 0; i < arr.length; i++) {
        // 迭代访问 arr[i]
    }
}

/* 基本的单链表节点 */
class ListNode {
    int val;
    ListNode next;
}

void traverse(ListNode head) {
    for (ListNode p = head; p != null; p = p.next) {
        // 迭代访问 p.val
    }
}

void traverse(ListNode head) {
    // 递归访问 head.val
    traverse(head.next)
}

/* 基本的二叉树节点 */
class TreeNode {
    int val;
    TreeNode left, right;
}

void traverse(TreeNode root) {
    traverse(root.left)
    traverse(root.right)
}

//刷二叉树
void traverse(TreeNode root) {
    // 前序遍历
    traverse(root.left)
    // 中序遍历
    traverse(root.right)
    // 后序遍历
}
```







