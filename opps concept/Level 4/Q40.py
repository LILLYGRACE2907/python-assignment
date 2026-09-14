# Question 40
# A Company has Employees. Identify the relationship and implement it.

# Relationship: HAS-A

class Employee:
    def show(self):
        print("Employee object")

class Company:
    def __init__(self):
        self.item = Employee()

    def show(self):
        print("Company has a Employee")
        self.item.show()

obj = Company()
obj.show()
