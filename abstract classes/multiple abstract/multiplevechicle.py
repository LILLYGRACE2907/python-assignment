from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car starts with a key")

    def stop(self):
        print("Car stops")


class Bike(Vehicle):

    def start(self):
        print("Bike starts with a button")

    def stop(self):
        print("Bike stops")


car = Car()
car.start()
car.stop()

bike = Bike()
bike.start()
bike.stop()