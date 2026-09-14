# Question 7
# Create an Animal class with a method sound() and override it in Dog and Cat.

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog says: Woof")

class Cat(Animal):
    def sound(self):
        print("Cat says: Meow")

Dog().sound()
Cat().sound()
