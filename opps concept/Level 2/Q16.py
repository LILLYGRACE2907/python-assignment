# Question 16
# Create a Department class that HAS-A multiple Employee objects.

class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self):
        self.employees = []

    def add_employee(self, obj):
        self.employees.append(obj)

    def show_employees(self):
        print("Department contains:", [x.name for x in self.employees])

obj = Department()
obj.add_employee(Employee("Example 1"))
obj.add_employee(Employee("Example 2"))
obj.show_employees()
