class Student:
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count = Student.count + 1


s1 = Student("Lilly")
s2 = Student("Anu")
s3 = Student("Ravi")

print("Total Students:", Student.count)