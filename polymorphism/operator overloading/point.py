class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def display(self):
        print("Point:", self.x, self.y)


p1 = Point(10, 20)
p2 = Point(5, 10)

p3 = p1 + p2
p3.display()