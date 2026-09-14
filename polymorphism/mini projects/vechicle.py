class Vehicle:
    def start(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car starts with a key")


class Bike(Vehicle):
    def start(self):
        print("Bike starts with a self-start")


class Bus(Vehicle):
    def start(self):
        print("Bus starts with an engine")


class Truck(Vehicle):
    def start(self):
        print("Truck starts with a powerful engine")


vehicles = [Car(), Bike(), Bus(), Truck()]

for vehicle in vehicles:
    vehicle.start()