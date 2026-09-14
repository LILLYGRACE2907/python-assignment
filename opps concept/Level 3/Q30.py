# Question 30
# Create a Course class and a CertificateGenerator class. Make the course USE-A the certificate generator.

class CertificateGenerator:
    def generate(self, name):
        print("CertificateGenerator:", name)

class Course:
    def __init__(self, name):
        self.name = name

    def use_service(self, service):
        service.generate(self.name)

obj = Course("Example")
obj.use_service(CertificateGenerator())
