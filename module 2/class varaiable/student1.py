class Student:
    college_name = "ABC College"

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Student Name:", self.name)
        print("College Name:", Student.college_name)


s1 = Student("Lilly")
s2 = Student("Anu")

s1.display()
s2.display()