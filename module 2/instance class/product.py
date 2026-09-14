class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        total = self.price * self.quantity
        print(self.name, "Total Price =", total)


p1 = Product("Pen", 10, 5)
p2 = Product("Book", 50, 3)
p3 = Product("Bag", 500, 2)

p1.total_price()
p2.total_price()
p3.total_price()