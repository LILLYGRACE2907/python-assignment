class Car:
    company = "Toyota"
    number_of_wheels = 4

    def __init__(self, model, price):
        self.model = model
        self.price = price

    def display(self):
        print("Company:", Car.company)
        print("Model:", self.model)
        print("Price:", self.price)
        print("Wheels:", Car.number_of_wheels)
        print()


c1 = Car("Fortuner", 4000000)
c2 = Car("Innova", 3000000)
c3 = Car("Glanza", 1000000)

c1.display()
c2.display()
c3.display()