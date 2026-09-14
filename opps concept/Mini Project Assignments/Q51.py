# Question 51
# Build a Library Management System demonstrating IS-A, HAS-A, and USES-A relationships.

# Library Management System
# Demonstrates IS-A, HAS-A and USES-A relationships.

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def study(self):
        print(self.name, "is studying")

class Book:
    def __init__(self, name):
        self.name = name

class SearchService:
    def use(self):
        print("SearchService used successfully")

class Library:
    def __init__(self):
        self.items = [Book("Item 1"), Book("Item 2")]

    def show_items(self):
        print("Items:", [x.name for x in self.items])

    def perform_service(self):
        SearchService().use()

# Example IS-A
student = Student("Lilly")
student.study()

# Example HAS-A and USES-A
system = Library()
system.show_items()
system.perform_service()
