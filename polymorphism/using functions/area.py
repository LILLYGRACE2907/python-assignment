class Circle:
    def area(self):
        print("Area of Circle")


class Rectangle:
    def area(self):
        print("Area of Rectangle")


class Triangle:
    def area(self):
        print("Area of Triangle")


def calculate_area(shape):
    shape.area()


circle = Circle()
rectangle = Rectangle()
triangle = Triangle()

calculate_area(circle)
calculate_area(rectangle)
calculate_area(triangle)