class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print(self.name, self.age, self.course)


s1 = Student("Lilly", 18, "CCN")
s2 = Student("Anu", 19, "CSE")
s3 = Student("Ravi", 18, "ECE")

s1.display()
s2.display()
s3.display()