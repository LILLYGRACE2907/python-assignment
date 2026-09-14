# Question 19
# Create a ShoppingCart class that HAS-A multiple Product objects.

class Product:
    def __init__(self, name):
        self.name = name

class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, obj):
        self.products.append(obj)

    def show_products(self):
        print("ShoppingCart contains:", [x.name for x in self.products])

obj = ShoppingCart()
obj.add_product(Product("Example 1"))
obj.add_product(Product("Example 2"))
obj.show_products()
