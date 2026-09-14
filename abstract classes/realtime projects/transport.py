from abc import ABC, abstractmethod

class Transport(ABC):

    @abstractmethod
    def travel(self):
        pass


class Bus(Transport):

    def travel(self):
        print("Travel by Bus")


class Train(Transport):

    def travel(self):
        print("Travel by Train")


class Flight(Transport):

    def travel(self):
        print("Travel by Flight")


class Cab(Transport):

    def travel(self):
        print("Travel by Cab")


Bus().travel()
Train().travel()
Flight().travel()
Cab().travel()