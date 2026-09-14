# Question 47
# Create a Company that HAS-A departments and employees and USES-A payroll service.

class Department:
    def __init__(self, name):
        self.name = name

class PayrollService:
    def use(self):
        print("PayrollService used")

class Company:
    def __init__(self):
        self.items = [Department("Item 1"), Department("Item 2")]

    def run(self):
        print("Company has:", [x.name for x in self.items])
        PayrollService().use()

obj = Company()
obj.run()
