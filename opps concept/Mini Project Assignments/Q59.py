# Question 59
# Build an Online Learning System with course relationships, student/teacher inheritance, and notification/certificate services.

# Online Learning System
# Demonstrates IS-A, HAS-A and USES-A relationships.

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def study(self):
        print(self.name, "is studying")

class Course:
    def __init__(self, name):
        self.name = name

class NotificationService:
    def use(self):
        print("NotificationService used successfully")

class LearningSystem:
    def __init__(self):
        self.items = [Course("Item 1"), Course("Item 2")]

    def show_items(self):
        print("Items:", [x.name for x in self.items])

    def perform_service(self):
        NotificationService().use()

# Example IS-A
student = Student("Lilly")
student.study()

# Example HAS-A and USES-A
system = LearningSystem()
system.show_items()
system.perform_service()
