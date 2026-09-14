# Question 45
# Create a ShoppingCart that HAS-A products and USES-A payment gateway.

class Product:
    def __init__(self, name):
        self.name = name

class PaymentGateway:
    def use(self):
        print("PaymentGateway used")

class ShoppingCart:
    def __init__(self):
        self.items = [Product("Item 1"), Product("Item 2")]

    def run(self):
        print("ShoppingCart has:", [x.name for x in self.items])
        PaymentGateway().use()

obj = ShoppingCart()
obj.run()
