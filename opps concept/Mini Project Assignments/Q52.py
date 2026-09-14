# Question 52
# Build a Banking System demonstrating account inheritance, customer relationships, and payment services.

# Banking System
# Demonstrates IS-A, HAS-A and USES-A relationships.

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def study(self):
        print(self.name, "is studying")

class Customer:
    def __init__(self, name):
        self.name = name

class PaymentService:
    def use(self):
        print("PaymentService used successfully")

class Bank:
    def __init__(self):
        self.items = [Customer("Item 1"), Customer("Item 2")]

    def show_items(self):
        print("Items:", [x.name for x in self.items])

    def perform_service(self):
        PaymentService().use()

# Example IS-A
student = Student("Lilly")
student.study()

# Example HAS-A and USES-A
system = Bank()
system.show_items()
system.perform_service()
