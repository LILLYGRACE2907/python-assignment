class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __add__(self, other):
        return self.price + other.price


p1 = Product("Laptop", 50000)
p2 = Product("Mouse", 1000)

total = p1 + p2

print("Combined Price:", total)