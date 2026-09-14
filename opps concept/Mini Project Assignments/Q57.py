# Question 57
# Build a Food Delivery System with order inheritance, restaurant HAS-A menu items, and order USES-A payment/delivery services.

# Food Delivery System
# Demonstrates IS-A, HAS-A and USES-A relationships.

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def study(self):
        print(self.name, "is studying")

class MenuItem:
    def __init__(self, name):
        self.name = name

class DeliveryService:
    def use(self):
        print("DeliveryService used successfully")

class Restaurant:
    def __init__(self):
        self.items = [MenuItem("Item 1"), MenuItem("Item 2")]

    def show_items(self):
        print("Items:", [x.name for x in self.items])

    def perform_service(self):
        DeliveryService().use()

# Example IS-A
student = Student("Lilly")
student.study()

# Example HAS-A and USES-A
system = Restaurant()
system.show_items()
system.perform_service()
