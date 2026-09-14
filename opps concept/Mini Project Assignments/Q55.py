# Question 55
# Build a School Management System with Person → Student/Teacher inheritance, school HAS-A students/teachers, and notification services.

# School Management System
# Demonstrates IS-A, HAS-A and USES-A relationships.

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def study(self):
        print(self.name, "is studying")

class Student:
    def __init__(self, name):
        self.name = name

class NotificationService:
    def use(self):
        print("NotificationService used successfully")

class School:
    def __init__(self):
        self.items = [Student("Item 1"), Student("Item 2")]

    def show_items(self):
        print("Items:", [x.name for x in self.items])

    def perform_service(self):
        NotificationService().use()

# Example IS-A
student = Student("Lilly")
student.study()

# Example HAS-A and USES-A
system = School()
system.show_items()
system.perform_service()
