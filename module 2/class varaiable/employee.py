class Employee:
    company_name = "TCS"

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)
        print("Company:", Employee.company_name)


e1 = Employee("Ravi")
e2 = Employee("Anu")
e3 = Employee("Kiran")

e1.display()
e2.display()
e3.display()