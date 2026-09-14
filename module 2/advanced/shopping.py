class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, name, price):
        self.products.append([name, price])

    def total_bill(self):
        total = 0

        for product in self.products:
            total = total + product[1]

        return total


cart = ShoppingCart()

cart.add_product("Book", 200)
cart.add_product("Pen", 50)
cart.add_product("Bag", 500)

print("Total Bill:", cart.total_bill())