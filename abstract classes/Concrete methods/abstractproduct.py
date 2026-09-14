from abc import ABC, abstractmethod

class Product(ABC):

    @abstractmethod
    def calculate_discount(self):
        pass

    def display_product(self):
        print("Product: Laptop")


class Laptop(Product):

    def calculate_discount(self):
        print("Discount: 10%")


p = Laptop()
p.calculate_discount()
p.display_product()