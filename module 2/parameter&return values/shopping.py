class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, name, price):
        self.products.append([name, price])
        print(name, "added")

    def remove_product(self, name):
        for product in self.products:
            if product[0] == name:
                self.products.remove(product)
                print(name, "removed")
                return

        print("Product not found")

    def total(self):
        total = 0

        for product in self.products:
            total = total + product[1]

        return total


cart = ShoppingCart()

cart.add_product("Book", 200)
cart.add_product("Pen", 50)
cart.add_product("Bag", 500)

cart.remove_product("Pen")

print("Total:", cart.total())