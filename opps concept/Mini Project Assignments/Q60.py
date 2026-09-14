# Question 60
# Build a complete OOP project demonstrating all three relationships: IS-A + HAS-A + USES-A, with at least 8 classes.

# Complete OOP Project
# Demonstrates IS-A, HAS-A and USES-A relationships.

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def study(self):
        print(self.name, "is studying")

class Product:
    def __init__(self, name):
        self.name = name

class PaymentService:
    def use(self):
        print("PaymentService used successfully")

class BusinessSystem:
    def __init__(self):
        self.items = [Product("Item 1"), Product("Item 2")]

    def show_items(self):
        print("Items:", [x.name for x in self.items])

    def perform_service(self):
        PaymentService().use()

# Example IS-A
student = Student("Lilly")
student.study()

# Example HAS-A and USES-A
system = BusinessSystem()
system.show_items()
system.perform_service()
