class Car:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def display(self):
        print(self.brand, self.model, self.year, self.price)


c1 = Car("Toyota", "Fortuner", 2023, 4000000)
c2 = Car("Honda", "City", 2022, 1500000)
c3 = Car("Hyundai", "Creta", 2024, 1800000)

c1.display()
c2.display()
c3.display()