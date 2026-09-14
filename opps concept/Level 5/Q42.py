# Question 42
# Create a Person → Student inheritance hierarchy and make Student HAS-A Course.

class Person:
    def show(self):
        print("Person")

class Course:
    def study(self):
        print("Course is being studied")

class Student(Person):
    def __init__(self):
        self.course = Course()

    def learn(self):
        self.course.study()

s = Student()
s.show()
s.learn()
