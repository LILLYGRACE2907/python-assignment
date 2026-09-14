from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    def display_info(self):
        print("This is a vehicle")


class Car(Vehicle):

    def start(self):
        print("Car starts with a key")


v = Car()
v.start()
v.display_info()