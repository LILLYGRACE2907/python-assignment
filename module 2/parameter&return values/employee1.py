class Employee:

    def __init__(self, name, daily_salary):
        self.name = name
        self.daily_salary = daily_salary

    def calculate_salary(self, working_days):
        return self.daily_salary * working_days


e = Employee("Ravi", 1000)

result = e.calculate_salary(25)

print("Employee:", e.name)
print("Salary:", result)