import math

class Shape:
    def area(self):
        print("Area of shape")


class Rectangle(Shape):
    def area(self):
        length = 10
        width = 5
        print("Rectangle Area:", length * width)


class Circle(Shape):
    def area(self):
        radius = 7
        print("Circle Area:", math.pi * radius * radius)


class Triangle(Shape):
    def area(self):
        base = 10
        height = 6
        print("Triangle Area:", 0.5 * base * height)


shapes = [Rectangle(), Circle(), Triangle()]

for shape in shapes:
    shape.area()