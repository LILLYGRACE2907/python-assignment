import math

class Shape:
    def area(self):
        pass


class Circle(Shape):
    def area(self):
        r = 5
        return math.pi * r * r


class Rectangle(Shape):
    def area(self):
        return 10 * 5


class Square(Shape):
    def area(self):
        return 6 * 6


class Triangle(Shape):
    def area(self):
        return 0.5 * 10 * 8


shapes = [Circle(), Rectangle(), Square(), Triangle()]

for shape in shapes:
    print("Area:", shape.area())