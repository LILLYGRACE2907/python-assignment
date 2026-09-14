class Duck:
    def walk(self):
        print("Duck is walking")


class Dog:
    def walk(self):
        print("Dog is walking")


def make_walk(animal):
    animal.walk()


d = Duck()
dog = Dog()

make_walk(d)
make_walk(dog)