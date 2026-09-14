class Car:
    def start(self):
        print("Car starts with a key")


class Bike:
    def start(self):
        print("Bike starts with a button")


class Bus:
    def start(self):
        print("Bus starts with a switch")


vehicles = [Car(), Bike(), Bus()]

for vehicle in vehicles:
    vehicle.start()