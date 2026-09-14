class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_cost(self):
        return self.price * self.quantity


p = Product("Laptop", 50000, 2)

print("Product:", p.name)
print("Total Cost:", p.total_cost())