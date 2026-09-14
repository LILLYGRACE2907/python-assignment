# Question 46
# Create a Hospital that HAS-A doctors and patients and USES-A billing service.

class Patient:
    def __init__(self, name):
        self.name = name

class BillingService:
    def use(self):
        print("BillingService used")

class Hospital:
    def __init__(self):
        self.items = [Patient("Item 1"), Patient("Item 2")]

    def run(self):
        print("Hospital has:", [x.name for x in self.items])
        BillingService().use()

obj = Hospital()
obj.run()
