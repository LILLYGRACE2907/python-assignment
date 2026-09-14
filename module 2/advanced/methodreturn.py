class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class College:
    def get_student(self, student):
        return student.name + " " + str(student.age)


s = Student("Lilly", 18)

c = College()

print(c.get_student(s))