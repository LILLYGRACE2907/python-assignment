# Question 32
# A Car has an Engine. Identify the relationship and implement it.

# Relationship: HAS-A

class Engine:
    def show(self):
        print("Engine object")

class Car:
    def __init__(self):
        self.item = Engine()

    def show(self):
        print("Car has a Engine")
        self.item.show()

obj = Car()
obj.show()
