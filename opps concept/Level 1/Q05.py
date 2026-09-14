# Question 5
# Create a Shape class and a Rectangle class using inheritance.

class Shape:
    def show(self):
        print("This is a shape")

class Rectangle(Shape):
    def area(self, length, width):
        print("Area =", length * width)

r = Rectangle()
r.show()
r.area(10, 5)
