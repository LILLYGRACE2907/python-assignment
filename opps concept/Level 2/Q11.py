# Question 11
# Create a Car class that HAS-A Engine object.

class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start_car(self):
        self.engine.start()
        print("Car started")

Car().start_car()
