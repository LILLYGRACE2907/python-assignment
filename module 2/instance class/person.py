class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("City:", self.city)
        print()


p1 = Person("Lilly", 18, "Kakinada")
p2 = Person("Anu", 19, "Vijayawada")

p1.display()
p2.display()