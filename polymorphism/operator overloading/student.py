class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks


s1 = Student("Lilly", 90)
s2 = Student("Grace", 85)

if s1 > s2:
    print(s1.name, "has higher marks")
else:
    print(s2.name, "has higher marks")