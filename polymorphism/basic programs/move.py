class Bird:
    def move(self):
        print("Bird flies")


class Dog:
    def move(self):
        print("Dog walks")


class Fish:
    def move(self):
        print("Fish swims")


animals = [Bird(), Dog(), Fish()]

for animal in animals:
    animal.move()