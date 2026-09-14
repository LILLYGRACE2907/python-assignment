# Question 15
# Create a College class that HAS-A multiple Student objects.

class Student:
    def __init__(self, name):
        self.name = name

class College:
    def __init__(self):
        self.students = []

    def add_student(self, obj):
        self.students.append(obj)

    def show_students(self):
        print("College contains:", [x.name for x in self.students])

obj = College()
obj.add_student(Student("Example 1"))
obj.add_student(Student("Example 2"))
obj.show_students()
