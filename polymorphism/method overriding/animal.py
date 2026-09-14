class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog says Woof")


class Cat(Animal):
    def sound(self):
        print("Cat says Meow")


class Cow(Animal):
    def sound(self):
        print("Cow says Moo")


animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.sound()