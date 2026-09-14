# Question 2
# Create an Animal class and a Dog class that demonstrates an IS-A relationship.

class Animal:
    def eat(self):
        print("Animal eats")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

dog = Dog()
dog.eat()
dog.bark()
