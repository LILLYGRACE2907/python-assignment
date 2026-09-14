from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def display_details(self):
        pass


class Manager(Employee):

    def calculate_salary(self):
        return 50000

    def display_details(self):
        print("Employee: Manager")
        print("Salary:", self.calculate_salary())


class Developer(Employee):

    def calculate_salary(self):
        return 40000

    def display_details(self):
        print("Employee: Developer")
        print("Salary:", self.calculate_salary())


manager = Manager()
manager.display_details()

developer = Developer()
developer.display_details()