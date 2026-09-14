from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    def display_shape(self):
        print("This is a shape")


class Circle(Shape):

    def area(self):
        print("Area of circle = 78.5")


s = Circle()
s.area()
s.display_shape()