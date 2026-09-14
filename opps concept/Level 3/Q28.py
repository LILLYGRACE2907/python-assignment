# Question 28
# Create a Hospital class and a BillingService class. Make the hospital USE-A the billing service.

class BillingService:
    def bill(self, name):
        print("BillingService:", name)

class Hospital:
    def __init__(self, name):
        self.name = name

    def use_service(self, service):
        service.bill(self.name)

obj = Hospital("Example")
obj.use_service(BillingService())
