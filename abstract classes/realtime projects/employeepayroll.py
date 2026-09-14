from abc import ABC, abstractmethod

class EmployeePayroll(ABC):

    @abstractmethod
    def salary(self):
        pass


class FullTimeEmployee(EmployeePayroll):

    def salary(self):
        print("Full time salary: 50000")


class PartTimeEmployee(EmployeePayroll):

    def salary(self):
        print("Part time salary: 20000")


class ContractEmployee(EmployeePayroll):

    def salary(self):
        print("Contract salary: 30000")


FullTimeEmployee().salary()
PartTimeEmployee().salary()
ContractEmployee().salary()