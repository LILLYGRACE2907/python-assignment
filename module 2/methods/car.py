class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def start(self):
        print("Car Started")

    def stop(self):
        print("Car Stopped")

    def display_details(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)


c = Car("Toyota", "Fortuner", 4000000)

c.display_details()
c.start()
c.stop()