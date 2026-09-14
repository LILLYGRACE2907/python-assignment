# Question 33
# A Student uses a Printer. Identify the relationship and implement it.

# Relationship: USES-A

class Printer:
    def use(self):
        print("Printer service used")

class Student:
    def do_work(self, service):
        print("Student uses Printer")
        service.use()

obj = Student()
obj.do_work(Printer())
