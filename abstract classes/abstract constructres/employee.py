from abc import ABC, abstractmethod

class Employee(ABC):

    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    @abstractmethod
    def calculate_salary(self):
        pass


class Manager(Employee):

    def calculate_salary(self):
        print("Manager Salary: Rs. 50000")


m = Manager("Lilly", 101)

print("Name:", m.name)
print("Employee ID:", m.employee_id)
m.calculate_salary()