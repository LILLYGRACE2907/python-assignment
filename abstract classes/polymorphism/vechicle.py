from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


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