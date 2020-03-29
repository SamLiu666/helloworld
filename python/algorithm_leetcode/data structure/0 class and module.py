from math import pi


class Shape:

    def __init__(self, color):
        # initialize method
        self.color = color

    def getColor(self):
        return self.color

    def __str__(self):
        # 字符串方法
        return self.getColor() + ' Shap'


# child inheritance
class Rectangle(Shape):

    def __init__(self, color, length, width):
        super().__init__(color)   # call father method
        self.length = length
        self.width = width

    def getArea(self):
        return self.width * self.length

    def getPerimeter(self):
        return 2 * (self.width + self.length)

    def __str__(self):
        return self.getColor() +  ' ' + type(self).__name__


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def getArea(self):
        return pi * self.radius ** 2

    def getPerimeter(self):
        return self.radius * pi * 2


# polymorphic
def print_shape_data(self):
    print('shap: ', type(self).__name__,
          'color: ', self.getColor(),
          'Area: ', self.getArea(),
          'Perimeter: ', self.getPerimeter(), sep='     ')


shape = Shape('blue')
print(shape.getColor(), shape.__str__())

newShape = Rectangle('blue', 5 , 4)
print_shape_data(newShape)