class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

    def display(self):
        print(self.name, self.department, self.salary)


e1 = Employee("Ravi", "IT", 30000)
e2 = Employee("Anu", "HR", 35000)
e3 = Employee("Kiran", "Sales", 28000)
e4 = Employee("Priya", "Finance", 40000)
e5 = Employee("Suresh", "IT", 45000)

e1.display()
e2.display()
e3.display()
e4.display()
e5.display()