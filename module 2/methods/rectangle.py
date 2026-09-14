class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Area:", self.length * self.width)

    def perimeter(self):
        print("Perimeter:", 2 * (self.length + self.width))


r = Rectangle(10, 5)

r.area()
r.perimeter()