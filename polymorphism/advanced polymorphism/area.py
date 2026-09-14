from abc import ABC, abstractmethod
import math


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Circle Area:", math.pi * self.radius * self.radius)


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print("Rectangle Area:", self.length * self.breadth)


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        print("Triangle Area:", 0.5 * self.base * self.height)


c = Circle(5)
r = Rectangle(10, 5)
t = Triangle(10, 6)

c.area()
r.area()
t.area()