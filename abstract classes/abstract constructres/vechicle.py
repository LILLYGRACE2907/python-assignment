from abc import ABC, abstractmethod

class Vehicle(ABC):

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")


c = Car("Toyota", "Innova")

print("Brand:", c.brand)
print("Model:", c.model)
c.start()
c.stop()