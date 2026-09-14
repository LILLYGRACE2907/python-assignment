# Question 10
# Create an Employee class and derive Developer, Tester, and Manager classes.

class Employee:
    def work(self):
        print("Employee works")

class Developer(Employee):
    def work(self):
        print("Developer writes code")

class Tester(Employee):
    def work(self):
        print("Tester tests software")

class Manager(Employee):
    def work(self):
        print("Manager manages the team")

for employee in [Developer(), Tester(), Manager()]:
    employee.work()
