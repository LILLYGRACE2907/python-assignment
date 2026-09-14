class Calculator:

    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        return a / b


c = Calculator()

print("Addition:", c.addition(10, 5))
print("Subtraction:", c.subtraction(10, 5))
print("Multiplication:", c.multiplication(10, 5))
print("Division:", c.division(10, 5))