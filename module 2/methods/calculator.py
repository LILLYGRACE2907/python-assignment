class Calculator:
    def addition(self, a, b):
        print("Addition:", a + b)

    def subtraction(self, a, b):
        print("Subtraction:", a - b)

    def multiplication(self, a, b):
        print("Multiplication:", a * b)

    def division(self, a, b):
        print("Division:", a / b)


c = Calculator()

c.addition(10, 5)
c.subtraction(10, 5)
c.multiplication(10, 5)
c.division(10, 5)