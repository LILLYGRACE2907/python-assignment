class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity


p = Product("Book", 200, 5)

print("Product:", p.name)
print("Total Price:", p.total_price())