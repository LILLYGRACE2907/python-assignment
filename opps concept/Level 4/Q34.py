# Question 34
# A Manager is an Employee. Identify the relationship and implement it.

# Relationship: IS-A

class Employee:
    def show(self):
        print("This is Employee")

class Manager(Employee):
    def action(self):
        print("This is Manager")

obj = Manager()
obj.show()
obj.action()
