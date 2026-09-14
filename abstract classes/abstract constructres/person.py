from abc import ABC, abstractmethod

class Person(ABC):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def work(self):
        pass


class Student(Person):

    def work(self):
        print(self.name, "is studying")


class Teacher(Person):

    def work(self):
        print(self.name, "is teaching")


class Doctor(Person):

    def work(self):
        print(self.name, "is treating patients")


s = Student("Lilly", 18)
t = Teacher("Ravi", 35)
d = Doctor("Anil", 40)

s.work()
t.work()
d.work()