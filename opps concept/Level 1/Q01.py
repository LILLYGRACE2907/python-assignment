# Question 1
# Create a Vehicle class and a Car class that demonstrates an IS-A relationship.

class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

car = Car()
car.move()
car.drive()
