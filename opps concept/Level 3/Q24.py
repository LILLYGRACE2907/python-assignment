# Question 24
# Create an Employee class and a ReportGenerator class. Make the employee USE-A the report generator.

class ReportGenerator:
    def generate(self, name):
        print("ReportGenerator:", name)

class Employee:
    def __init__(self, name):
        self.name = name

    def use_service(self, service):
        service.generate(self.name)

obj = Employee("Example")
obj.use_service(ReportGenerator())
