# Question 17
# Create a School class that HAS-A Teacher and Student objects.

class Teacher:
    def __init__(self, name):
        self.name = name

class School:
    def __init__(self):
        self.teachers = []

    def add_teacher(self, obj):
        self.teachers.append(obj)

    def show_teachers(self):
        print("School contains:", [x.name for x in self.teachers])

obj = School()
obj.add_teacher(Teacher("Example 1"))
obj.add_teacher(Teacher("Example 2"))
obj.show_teachers()
