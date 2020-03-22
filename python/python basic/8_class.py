from math import sqrt
from time import time, localtime, sleep
"""learning class """


# the definition of class: student
class student():
    # __init__ 特殊方法创建对象时进行初始化操作
    def __init__(self, name, age, height=181):
        # default of height is 181
        # __name for private value
        self._name, self._age = name, age
        # private value
        self._height = height

    def learning(self, course):
        print(self._name + ' is learning ' + course)

    def activities(self):
        if (self._height > 180):
            print(self._name + ' is playing basketball. ')
        else:
            print(self._name + ' is doing nothing.')

    # private method
    def __barr(self):
        print('private')


# static method for triangle class
class Triangle(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) *
                    (half - self._b) * (half - self._c))


# Clock class
class Clock(object):
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)


# Build and use a class
def test():
    stu_1 = student('Ming He', 15, 178)
    stu_1.learning('action movies')
    stu_1.activities()
    stu_1._student__barr()  # access to the private method

# present time until end
def display_time():

    clock = Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


if __name__ == '__main__':
    # display_time()
    pass
