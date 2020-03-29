def List_String():
    """字符串、列表操作"""
    str = "  Hello,223, 22 every one 1 and good !  "
    print(
        str,
        '0', len(str),  # 字符串长度
        '1', str.capitalize(),  # 字符串首字母大写
        '2', str.upper(),  # 字符串全部大写
        '3', str.find('one'),  # 找字串所在位置
        '4', str.startswith('Helo'),  # 检查字符串是否以指定字符开头
        '5', str.endswith('d'),  # 是否以指定字符结尾
        '6', str.center(50, '&'),  # 将字符串以指定的宽度居中并在两侧填充指定的字符
        '7', str.isalpha(),  # 字符串是否全是以字母组成
        '8', str.isalnum(),  # 字符串是否全是以数字组成
        '9', str[2:8],  # 字符串切片(从指定的开始索引到指定的结束索引)
        '10', str.strip(),  # 修剪左右两侧空格的拷贝
        sep='\n', end='\n',
    )
    print('\n')
    # 列表
    list1 = [21, 3, 15, 7, 9, 102]
    list2 = ['heihei'] * 6
    print(
        '0', len(list1),  # 列表长度
        '1', list1[4],  # 下标寻找元素
        '2', list1.append(20), list1,  # 将元素添加到列表最后
        '3', list2.insert(3, '30'), list2,  # 将元素添加到指定位置
        '4', list1.remove(3), list1,  # 删除指定元素'3'，若没有则执行不了
        '5', list1.pop(), list1,  # 弹出最后一个元素
        '6', list1.sort(), list1,  # 排序不可逆
        '7', tuple(list1),  # 列表转换为元组（不可变的数据类型）
        '8', set(list2), list2,  # 集合（不含重复元素）
        sep='\n', end='\n',
    )


def Tuple():
    """tuple opreation"""
    print('*** tuple ***')
    tup = ()        # immutable
    tup_1 = (1,2,3,4,3)
    tup_2 = 1,[3,2],    # can change the element list in tuple
    print(tup_2)
    tup_2[1][1] = 0
    print(type(tup),type(tup_2),tup,tup_1,tup_2)


def Set():
    tup_1 = [11.2,22,3,3,1]
    print('*** set ***')
    x = {1,3,3,4,5,6,6}
    a = set()
    b = set(tup_1)
    a.add(55)
    b.remove(1) #
    x.pop()
    print(x,a,b)


def Dictionary():
    print('*** dict ***')
    # 字典，键值对结构
    scores = {'小明': 95, '小张': 78, '小王': 82}
    print(

        '0', scores['小明'],  # 字典访问数据，通过键的方式
        '1', scores.get('小明', ),  # 通过get方法并设置默认值
        '2', scores.pop("小张"), scores,  # 弹出元素
        '3', scores.popitem(), scores,  # 弹出最后一个元素
        '4', scores.clear(), scores,  # 清空字典
        sep='\n', end='\n',
    )
    # scores['小明'] = 100
    # scores['小明'] = 50
    print(' ')
    scores = {'小明': 95, '小张': 78, '小王': 82}
    scores['小明'] = 100
    print(scores.keys(),    # 字典键
          scores.values(),  # 字典值
          scores.items()    # 字典 键值对 元组
          )
    print('小明' in scores.values(), 100 in scores.values(),
          '小明' in scores.keys(), 'a' in scores.items())
    print('迭代访问字典')
    for key in scores:
        print(key, scores[key])
    for key, value in scores:
        print(key, value)

if __name__ == '__main__':
    List_String()   # excute
