# Question 31
# A Dog is an Animal. Identify the relationship and implement it.

# Relationship: IS-A

class Animal:
    def show(self):
        print("This is Animal")

class Dog(Animal):
    def action(self):
        print("This is Dog")

obj = Dog()
obj.show()
obj.action()
