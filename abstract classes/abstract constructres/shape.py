from abc import ABC, abstractmethod

class Shape(ABC):

    def __init__(self, color):
        self.color = color

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):

    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    def area(self):
        print("Area:", self.length * self.width)


r = Rectangle("Red", 10, 5)

print("Color:", r.color)
r.area()