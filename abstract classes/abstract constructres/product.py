from abc import ABC, abstractmethod

class Product(ABC):

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def calculate_discount(self):
        pass


class Mobile(Product):

    def calculate_discount(self):
        discount = self.price * 0.10
        print("Discount:", discount)
        print("Final Price:", self.price - discount)


m = Mobile("Mobile Phone", 20000)

print("Product:", m.name)
print("Price:", m.price)
m.calculate_discount()