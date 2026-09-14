class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def total_price(self, quantity):
        return self.price * quantity


p = Product("Book", 200)

result = p.total_price(5)

print("Product:", p.name)
print("Total Price:", result)