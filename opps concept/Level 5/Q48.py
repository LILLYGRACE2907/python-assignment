# Question 48
# Create a School that HAS-A teachers and students and USES-A notification service.

class Student:
    def __init__(self, name):
        self.name = name

class NotificationService:
    def use(self):
        print("NotificationService used")

class School:
    def __init__(self):
        self.items = [Student("Item 1"), Student("Item 2")]

    def run(self):
        print("School has:", [x.name for x in self.items])
        NotificationService().use()

obj = School()
obj.run()
