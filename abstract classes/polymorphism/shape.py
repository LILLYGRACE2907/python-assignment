from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):

    def area(self):
        return 10 * 5


class Circle(Shape):

    def area(self):
        return 3.14 * 7 * 7


shapes = [Rectangle(), Circle()]

for shape in shapes:
    print("Area:", shape.area())