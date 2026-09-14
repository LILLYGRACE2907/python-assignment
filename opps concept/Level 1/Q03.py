# Question 3
# Create a Person class and a Student class using inheritance.

class Person:
    def introduce(self):
        print("I am a person")

class Student(Person):
    def study(self):
        print("Student is studying")

s = Student()
s.introduce()
s.study()
