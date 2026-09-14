# Question 37
# A Laptop has a Keyboard. Identify the relationship and implement it.

# Relationship: HAS-A

class Keyboard:
    def show(self):
        print("Keyboard object")

class Laptop:
    def __init__(self):
        self.item = Keyboard()

    def show(self):
        print("Laptop has a Keyboard")
        self.item.show()

obj = Laptop()
obj.show()
