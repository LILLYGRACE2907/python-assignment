 class Vehicle:
    def start(self):
        print("Vehicle starts")


class Car(Vehicle):
    def start(self):
        print("Car starts")


class Bike(Vehicle):
    def start(self):
        print("Bike starts")


class Bus(Vehicle):
    def start(self):
        print("Bus starts")


vehicles = [Car(), Bike(), Bus()]

for vehicle in vehicles:
    vehicle.start()