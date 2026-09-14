class Student:
    def __init__(self, name, m1, m2, m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def total_marks(self):
        return self.m1 + self.m2 + self.m3

    def average_marks(self):
        return self.total_marks() / 3


s = Student("Lilly", 80, 90, 85)

print("Name:", s.name)
print("Total Marks:", s.total_marks())
print("Average Marks:", s.average_marks())