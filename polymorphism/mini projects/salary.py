class Employee:
    def calculate_salary(self):
        pass


class Manager(Employee):
    def calculate_salary(self):
        return 60000


class Developer(Employee):
    def calculate_salary(self):
        return 50000


class Tester(Employee):
    def calculate_salary(self):
        return 40000


class Intern(Employee):
    def calculate_salary(self):
        return 15000


employees = [Manager(), Developer(), Tester(), Intern()]

for employee in employees:
    print("Salary:", employee.calculate_salary())