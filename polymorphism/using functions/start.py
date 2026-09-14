class Car:
    def start(self):
        print("Car started")


class Bike:
    def start(self):
        print("Bike started")


class Bus:
    def start(self):
        print("Bus started")


def start_vehicle(vehicle):
    vehicle.start()


car = Car()
bike = Bike()
bus = Bus()

start_vehicle(car)
start_vehicle(bike)
start_vehicle(bus)