class Dog:
    def sound(self):
        print("Dog says Woof")


class Cat:
    def sound(self):
        print("Cat says Meow")


class Cow:
    def sound(self):
        print("Cow says Moo")


def animal_sound(animal):
    animal.sound()


dog = Dog()
cat = Cat()
cow = Cow()

animal_sound(dog)
animal_sound(cat)
animal_sound(cow)