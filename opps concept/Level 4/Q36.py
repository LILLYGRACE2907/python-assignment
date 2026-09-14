# Question 36
# A ShoppingCart uses a PaymentGateway. Identify the relationship and implement it.

# Relationship: USES-A

class PaymentGateway:
    def use(self):
        print("PaymentGateway service used")

class ShoppingCart:
    def do_work(self, service):
        print("ShoppingCart uses PaymentGateway")
        service.use()

obj = ShoppingCart()
obj.do_work(PaymentGateway())
