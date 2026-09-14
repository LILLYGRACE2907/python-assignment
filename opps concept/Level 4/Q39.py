# Question 39
# An Order uses a PaymentService. Identify the relationship and implement it.

# Relationship: USES-A

class PaymentService:
    def use(self):
        print("PaymentService service used")

class Order:
    def do_work(self, service):
        print("Order uses PaymentService")
        service.use()

obj = Order()
obj.do_work(PaymentService())
