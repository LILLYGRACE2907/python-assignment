from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass

    def display_company(self):
        print("Company: ABC Company")


class Manager(Employee):

    def calculate_salary(self):
        print("Salary: 50000")


e = Manager()
e.calculate_salary()
e.display_company()