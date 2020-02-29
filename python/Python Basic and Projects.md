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

# GUI - Graphical User Interface
## Tkinter module
In python, tkinter - development kit
Steps: import what we need, create the gui window, write down the code, do the circulation
## Pygame module
This module is designed for the development of multimedia applications such as video games, based on [SDL](https://baike.baidu.com/item/SDL/224181?fr=aladdin)
