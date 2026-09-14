class Employee:
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def annual_salary(self):
        return self.monthly_salary * 12


e = Employee("Ravi", 30000)

print("Name:", e.name)
print("Annual Salary:", e.annual_salary())