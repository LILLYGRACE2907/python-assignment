# Question 49
# Create an OnlineOrder that HAS-A products and USES-A payment and delivery services.

class Product:
    def __init__(self, name):
        self.name = name

class PaymentService:
    def use(self):
        print("PaymentService used")

class OnlineOrder:
    def __init__(self):
        self.items = [Product("Item 1"), Product("Item 2")]

    def run(self):
        print("OnlineOrder has:", [x.name for x in self.items])
        PaymentService().use()

obj = OnlineOrder()
obj.run()

class DeliveryService:
    def deliver(self): print("Delivery service used")
