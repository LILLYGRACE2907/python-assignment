class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def __eq__(self, other):
        area1 = self.length * self.breadth
        area2 = other.length * other.breadth

        return area1 == area2


r1 = Rectangle(10, 5)
r2 = Rectangle(5, 10)

if r1 == r2:
    print("Both rectangles have the same area")
else:
    print("Areas are different")