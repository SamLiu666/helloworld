

![image-20200313223615643](C:\Users\liu\AppData\Roaming\Typora\typora-user-images\image-20200313223615643.png)

## Element of Sorting

callbacks  回调，任何数据类型的应用

### 选择排序 Selection Sort

与数组输入无关，算法复杂度始终O(N^2)

### 插入排序

交换次数与输入的逆序对个数有关

### Shellsort  希尔排序 

插入排序以单位距离移动，变化为移动h个距离



## 归并排序 Merge Sort

In-place 不消耗空间

没有比归并排序更优秀的算法

comparator 接口 去使用任何数据类型

归并排序和插入排序是稳定的

两类

#### Bottom -Up

#### Up-Bottom

## Heap definitions

Definition. A binary tree is heap-ordered if the key in each node is larger than or
equal to the keys in that node’s two children (if any).

A binary heap is a collection of keys arranged in a complete heap-ordered
binary tree, represented in level order in an array (not using the first entry).

Bottom-up reheapify ( swim). Top-down reheapify (sink).

![image-20200315174855304](C:\Users\liu\AppData\Roaming\Typora\typora-user-images\image-20200315174855304.png)