# Question 8
# Create a Person class with common details and derive Student and Teacher classes from it.

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def show(self):
        print("Student:", self.name)

class Teacher(Person):
    def show(self):
        print("Teacher:", self.name)

Student("Lilly").show()
Teacher("Anu").show()
