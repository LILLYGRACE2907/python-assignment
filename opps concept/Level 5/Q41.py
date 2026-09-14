# Question 41
# Create a Vehicle → Car inheritance hierarchy and make the Car HAS-A Engine.

class Vehicle:
    def move(self):
        print("Vehicle moves")

class Engine:
    def start(self):
        print("Engine starts")

class Car(Vehicle):
    def __init__(self):
        self.engine = Engine()

    def drive(self):
        self.engine.start()
        print("Car drives")

car = Car()
car.move()
car.drive()
