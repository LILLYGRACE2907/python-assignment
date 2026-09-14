# Question 25
# Create a Student class and a NotificationService class. Make the student USE-A the notification service.

class NotificationService:
    def send(self, name):
        print("NotificationService:", name)

class Student:
    def __init__(self, name):
        self.name = name

    def use_service(self, service):
        service.send(self.name)

obj = Student("Example")
obj.use_service(NotificationService())
