class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __gt__(self, other):
        return self.salary > other.salary


e1 = Employee("John", 50000)
e2 = Employee("David", 40000)

if e1 > e2:
    print(e1.name, "has higher salary")
else:
    print(e2.name, "has higher salary")