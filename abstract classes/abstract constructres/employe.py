from abc import ABC, abstractmethod

class Employee(ABC):

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @abstractmethod
    def work(self):
        pass


class Manager(Employee):

    def work(self):
        print(self.name, "is managing the team")


class Developer(Employee):

    def work(self):
        print(self.name, "is developing software")


class Tester(Employee):

    def work(self):
        print(self.name, "is testing software")


m = Manager("Ravi", 50000)
d = Developer("Anil", 40000)
t = Tester("Sita", 35000)

m.work()
d.work()
t.work()