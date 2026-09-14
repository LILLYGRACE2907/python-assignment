from abc import ABC, abstractmethod


class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass


class Manager(Employee):
    def calculate_salary(self):
        print("Manager Salary: 60000")


class Developer(Employee):
    def calculate_salary(self):
        print("Developer Salary: 50000")


class Tester(Employee):
    def calculate_salary(self):
        print("Tester Salary: 40000")


m = Manager()
d = Developer()
t = Tester()

m.calculate_salary()
d.calculate_salary()
t.calculate_salary()