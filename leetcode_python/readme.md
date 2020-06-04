# Recursion

哈希表：存储数据，优化计算

尾调用：返回递归函数，优化空间（C++ C， JAVA, PYTHON没有优化）

1. 有疑问时，写下递归关系
2. 重复计算，使用哈希存储记忆。**memoization**
3. 栈溢出，尾调用可尝试， **tail recursion**

# Median

## 48. Rotate Image

matrix -> Inverse -> symmetry

## 328. Odd Even Linked List - linked list



# Tree

# Binary search

### What is Binary Search?



Binary Search is one of the most fundamental and useful algorithms in Computer Science. It describes the process of searching for a specific value in an ordered collection.

> Terminology used in Binary Search:
>
> - Target - the value that you are searching for
> - Index - the current location that you are searching
> - Left, Right - the indicies from which we use to maintain our search Space
> - Mid - the index that we use to apply a condition to determine if we should search left or right

Other Binary Search Defintions:

------

Binary Search is generally composed of 3 main sections:

1. ***Pre-processing\*** - Sort if collection is unsorted.
2. ***Binary Search\*** - Using a loop or recursion to divide search space in half after each comparison.
3. ***Post-processing\*** - Determine viable candidates in the remaining space.

