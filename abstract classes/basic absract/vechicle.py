from abc import ABC, abstractmethod
class vechicle(ABC):
    @abstractmethod
    def start(self):
        pass

class car(vechicle):
    def start(self):
        print("Car is starting")
class bike(vechicle):
    def start(self):
        print("Bike is starting")
c=car()
b=bike()
c.start()
b.start()