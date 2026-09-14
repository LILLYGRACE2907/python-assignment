class Car:
    def start(self):
        print("Car started")


class Bike:
    def start(self):
        print("Bike started")


def start_vehicle(vehicle):
    vehicle.start()


car = Car()
bike = Bike()

start_vehicle(car)
start_vehicle(bike)