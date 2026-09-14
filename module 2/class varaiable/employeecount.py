class Employee:
    company_name = "Infosys"
    employee_count = 0

    def __init__(self, name):
        self.name = name
        Employee.employee_count = Employee.employee_count + 1

    def display(self):
        print("Name:", self.name)
        print("Company:", Employee.company_name)


e1 = Employee("Ravi")
e2 = Employee("Anu")
e3 = Employee("Kiran")

e1.display()
e2.display()
e3.display()

print("Total Employees:", Employee.employee_count)