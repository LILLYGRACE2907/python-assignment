import math

class Rectangle:
    def area(self):
        length = 10
        width = 5
        print("Rectangle Area:", length * width)


class Circle:
    def area(self):
        radius = 7
        print("Circle Area:", math.pi * radius * radius)


shapes = [Rectangle(), Circle()]

for shape in shapes:
    shape.area()