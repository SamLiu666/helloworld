# Python Basic and Projects
This project include some basic knowledge and small programmers. It is easy for beginners to practice.
To make it better, keep learning is necessary. 

## Class & Object oriented programming
object = data_structure + handle_method
class = object_0 + object_1 +... the same behavior of object as class 
Using encapsulation to hide details, inheritance for specialization and generalization
Polymorphism for type of dynamic class

## Adavance in Object oriented programming

## @property decorator 
This method, which is different from __ method, is used to nake the value of class private.
Use @getter to visit and @setter to change

### @__slots __ :magic method
__slots__ = ('_name', '_age')
the name and age of this class is only for _name, _age

### @staticmethod  static method
this method is used for the class not for object

## Inheritance 
Create a new class based on the old class, inheriting the father class's method and attributes.

### Abstract class
Abstract class can not create class including object. This class
is special for other class to inherit.
```python
from abc import ABCMeta, abstractmethod
class Hello:
    @abstractmethod
    def make(self):
        pass
```

## GUI - Graphical User Interface
### Tkinter module
In python, tkinter - development kit
Steps: import what we need, create the gui window, write down the code, do the circulation
### Pygame module
This module is designed for the development of multimedia applications such as video games, based on [SDL](https://baike.baidu.com/item/SDL/224181?fr=aladdin)

## File and Exception
[file system](https://baike.baidu.com/item/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/4827215?fr=aladdin) manages files
[reference](https://www.runoob.com/python3/python3-file-methods.html)
[HTTP knowledge](http://www.ruanyifeng.com/blog/2016/08/http.html)

## Regular expression
It is designed for handling strings and html and a tool defining the matching rules of strings.
[tutorial](https://deerchao.cn/tutorials/regex/regex.htm)
python for RE to support regular expression 

![image-20200229160755033](C:\Users\liu\AppData\Roaming\Typora\typora-user-images\image-20200229160755033.png)

## Processes and threads
### Process
Operating system divides memory based on process. Every process has own address.
Process is created by fork or spawn. The communication between process includes pipe, signal, socket and so on.
Unix and Linux has fork() to create process.
Python has multiprocessing importing Process
For threads,  use clock to protect the marginal resource
Method: 
```python
# Process
p1 = Process(target=download_task, args=('zz.pdf', ))
__Process__ class to creat object of process
__target__ function for code to run
__args__ tuple to pass to the target function
__start__ start the process
__join__ wait for the finishing

#Thread
t = threading.Thread(target = get_weather, args=(cities[i]
class Account(object):

    def __init__(self):
        self._balance = 0
        self._lock = Lock()
        
    def deposit(self, money):
        # get clock then do
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance
        finally:
            # release after done
            self._lock.release()
```
How to choose:
One is to consider the cost of task and the exchange of task.
Second is about the type of taks, which are compute-intensive and I/O intensive.
For coupute-intensive tasts cost cpu that is handled by language C. Scripting language like python is good for I/O intensive task. 
The single-threaded + asynchronous I/O programming model is called coroutine,[example](https://blog.csdn.net/qq_42672770/article/details/103798443)

