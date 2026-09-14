class Student:
    def display(self):
        print("Student: Lilly")
        print("Course: Python")


class Teacher:
    def display(self):
        print("Teacher: Ravi")
        print("Subject: Programming")


people = [Student(), Teacher()]

for person in people:
    person.display()