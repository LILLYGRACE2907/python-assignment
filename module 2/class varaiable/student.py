class Student:
    college_name = "ABC College"

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)
        print("College:", Student.college_name)


s1 = Student("Lilly")
s2 = Student("Anu")
s3 = Student("Ravi")

s1.display()
s2.display()
s3.display()