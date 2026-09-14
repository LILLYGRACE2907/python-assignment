# Question 43
# Create an Employee → Developer inheritance hierarchy and make Developer HAS-A Laptop.

class Employee:
    def work(self):
        print("Employee works")

class Laptop:
    def start(self):
        print("Laptop starts")

class Developer(Employee):
    def __init__(self):
        self.laptop = Laptop()

    def code(self):
        self.laptop.start()
        print("Developer writes code")

d = Developer()
d.work()
d.code()
