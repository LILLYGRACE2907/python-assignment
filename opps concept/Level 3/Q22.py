# Question 22
# Create a BankAccount class and a PaymentService class. Make the account USE-A the payment service.

class PaymentService:
    def pay(self, name):
        print("PaymentService:", name)

class BankAccount:
    def __init__(self, name):
        self.name = name

    def use_service(self, service):
        service.pay(self.name)

obj = BankAccount("Example")
obj.use_service(PaymentService())
