# Question 26
# Create an Order class and an EmailService class. Make the order USE-A the email service to send confirmation.

class EmailService:
    def send(self, name):
        print("EmailService:", name)

class Order:
    def __init__(self, name):
        self.name = name

    def use_service(self, service):
        service.send(self.name)

obj = Order("Example")
obj.use_service(EmailService())
