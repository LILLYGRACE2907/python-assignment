# Question 56
# Build a Vehicle Rental System with vehicle inheritance, rental HAS-A customer/vehicle, and payment service usage.

# Vehicle Rental System
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

class Rental:
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
system = Rental()
system.show_items()
system.perform_service()
