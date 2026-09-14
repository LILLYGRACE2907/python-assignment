from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass


class Manager(Employee):

    def calculate_salary(self):
        return 50000


class Developer(Employee):

    def calculate_salary(self):
        return 40000


class Tester(Employee):

    def calculate_salary(self):
        return 30000


employees = [Manager(), Developer(), Tester()]

for employee in employees:
    print("Salary:", employee.calculate_salary())