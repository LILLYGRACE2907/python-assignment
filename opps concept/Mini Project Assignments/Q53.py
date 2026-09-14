# Question 53
# Build a Hospital Management System using inheritance for different employees, HAS-A relationships for patients/doctors, and USES-A relationships for billing.

# Hospital Management System
# Demonstrates IS-A, HAS-A and USES-A relationships.

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def study(self):
        print(self.name, "is studying")

class Patient:
    def __init__(self, name):
        self.name = name

class BillingService:
    def use(self):
        print("BillingService used successfully")

class Hospital:
    def __init__(self):
        self.items = [Patient("Item 1"), Patient("Item 2")]

    def show_items(self):
        print("Items:", [x.name for x in self.items])

    def perform_service(self):
        BillingService().use()

# Example IS-A
student = Student("Lilly")
student.study()

# Example HAS-A and USES-A
system = Hospital()
system.show_items()
system.perform_service()
