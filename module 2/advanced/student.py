class Student:
    college = "ABC College"     # Class variable

    def __init__(self, name, age):
        self.name = name         # Instance variable
        self.age = age           # Instance variable

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("College:", Student.college)


s1 = Student("Lilly", 18)
s2 = Student("Ravi", 19)

s1.display()
s2.display()