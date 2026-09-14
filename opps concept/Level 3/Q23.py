# Question 23
# Create a ShoppingCart class and a PaymentGateway class. Make the shopping cart USE-A the payment gateway during checkout.

class PaymentGateway:
    def pay(self, name):
        print("PaymentGateway:", name)

class ShoppingCart:
    def __init__(self, name):
        self.name = name

    def use_service(self, service):
        service.pay(self.name)

obj = ShoppingCart("Example")
obj.use_service(PaymentGateway())
