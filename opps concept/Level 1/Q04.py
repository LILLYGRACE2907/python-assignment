# Question 4
# Create an Employee class and a Manager class using inheritance.

class Employee:
    def work(self):
        print("Employee is working")

class Manager(Employee):
    def manage(self):
        print("Manager is managing the team")

m = Manager()
m.work()
m.manage()
