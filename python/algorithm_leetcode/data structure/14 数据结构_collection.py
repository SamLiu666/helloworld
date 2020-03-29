from collections import Counter, deque, defaultdict

"""refe:  https://docs.python.org/3/library/collections.html#counter-objects"""

def Counter_info():
    print("**** 计数类型 Counter ****")
    c = Counter({'red': 4, 'blue': 2}) # 为计数器赋值，或 Counter('gallahad')
    cnt = Counter()     # 初始化计数器
    print("init= ", [3,2,2,3,5])
    for ch in [3,2,2,3,5]:
        cnt[ch] += 1
    visit = cnt[11]     # 字典 键值对访问机制
    print(cnt,type(cnt),c,visit)
    print("操作函数")
    seq = sorted(c.elements())  # c.elements() 返回所有计数器中的键组成的列表，可迭代
    print(seq, type(seq), end='\n')
    print('\n')


def Deque_Queue():
    print("**** Deque 实质双向队列 ****")
    d = deque("ascvrewiuo")
    print("** deque as stack LIFO**")
    d.appendleft(11) # add x to the left side of deque
    d.append(0) # Add x to the right side of the deque.
    print(d)
    d.pop()     # Remove and return an element from the right side of the deque. If no elements are present, raises an IndexError.
    print(d)
    print("** deque as queue FIFO**")
    d.append("first")
    print(d)
    d.popleft() # Remove and return an element from the left side of the deque. If no elements are present, raises an IndexError.
    print(d)
    print("* deque operation *")
    print(d.index('o')) # return the first match index of the element
    d.reverse() # return None, reverse the deque
    print(d, d.remove('a'), end='\n')     # remove return None, delete x

    print('\n')


def DefaultDict():
    # def Collection_defaultdic():
    print("**** DefaultDict 字典构成，可一键多值对 ****")
    s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
    print("initial = ", s )
    print("操作后：")

    create_d0 = defaultdict(dict)    # 用dict \ list 构造元素存储格式
    create_d1 = defaultdict(list)
    create_d2 = defaultdict(set)

    for k, v in s:
        create_d0[k]=v          # 字典添加元素方式
        create_d1[k].append(v)  # 列表添加元素方式
        create_d2[k].add(v)     #集合添加元素方式

    print(create_d0.items(),          #  字典
          create_d1,                  # 列表
          sorted(create_d2.items()),  # 集合
          create_d2,
            # d.item() 访问所有元素
          sep='\n', end='\n')


if __name__ == '__main__':
    Counter_deque()
    Counter_info()
    DefaultDict()