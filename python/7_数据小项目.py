import os,time
from random import randrange, randint, sample

def display():
    """跑马灯程序"""
    words ="I Love U "

    while True:
        os.system('cls')    #清楚屏幕上的输出
        print(words)

        #休眠时间
        time.sleep(0.2)
        words = words[1:] + words[0]

def get_lastname(file_name, has_dot = False):
    """
    获取文件名的或追命
    :param file_name: 文件名
    :param has_dot: 返回的文件后缀名是否要带点
    :return: 文件的后缀名
    """
    pos = file_name.rfind('.')  #返回字符串最后一次出现的位置(从右向左查询)，如果没有匹配项则返回-1
    if 0<pos<len(file_name)-1:
        index = pos if has_dot else pos+1
        return file_name[index:]
    else:
        return ''

def Yanghui_Triangle():
    num = int(input('Number of rows: '))
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()

def display(balls):
    """
    输出列表中的双色球号码
    """
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print('%02d' % ball, end=' ')
    print()


def random_select():
    """
    随机选择一组号码
    """
    red_balls = [x for x in range(1, 34)]
    selected_balls = []
    selected_balls = sample(red_balls, 7) #random模块的sample函数来实现从列表中选择不重复的n个元素
    selected_balls.sort()
    selected_balls.append(randint(1, 16))
    return selected_balls


def main():
    n = int(input('机选几注: '))
    for _ in range(n):
        display(random_select())

def YuessefulCircle():
    persons = [True] * 30
    counter, index, number = 0, 0, 0
    while counter < 15:
        if persons[index]:
            number += 1
            if number == 9:
                persons[index] = False
                counter += 1
                number = 0
        index += 1
        index %= 30
    for person in persons:
        print('基' if person else '非', end='')


if __name__ == '__main__':
    #display()
    # print(get_lastname("asdas.xlsx", True))
    # Yanghui_Triangle()
    # main()  #双色球选号
    YuessefulCircle()

