class ShoppingCart:
    def __init__(self, items):
        self.items = items

    def __add__(self, other):
        return ShoppingCart(self.items + other.items)

    def display(self):
        print("Shopping Cart:", self.items)


cart1 = ShoppingCart(["Laptop", "Mouse"])
cart2 = ShoppingCart(["Keyboard", "Headphones"])

cart3 = cart1 + cart2

cart3.display()