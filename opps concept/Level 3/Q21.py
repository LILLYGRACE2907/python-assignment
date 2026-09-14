# Question 21
# Create a Student class and a Printer class. Make the Student USE-A Printer to print student details.

class Printer:
    def print_details(self, name):
        print("Printer:", name)

class Student:
    def __init__(self, name):
        self.name = name

    def use_service(self, service):
        service.print_details(self.name)

obj = Student("Example")
obj.use_service(Printer())
