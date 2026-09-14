# Question 58
# Build a Company Management System with employee inheritance, company HAS-A departments/employees, and payroll USES-A payment services.

# Company Management System
# Demonstrates IS-A, HAS-A and USES-A relationships.

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def study(self):
        print(self.name, "is studying")

class Employee:
    def __init__(self, name):
        self.name = name

class PayrollService:
    def use(self):
        print("PayrollService used successfully")

class Company:
    def __init__(self):
        self.items = [Employee("Item 1"), Employee("Item 2")]

    def show_items(self):
        print("Items:", [x.name for x in self.items])

    def perform_service(self):
        PayrollService().use()

# Example IS-A
student = Student("Lilly")
student.study()

# Example HAS-A and USES-A
system = Company()
system.show_items()
system.perform_service()
