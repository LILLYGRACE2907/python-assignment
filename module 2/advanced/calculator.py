class Calculator:

    def add(self, a, b):
        return a + b

    def square(self, n):
        return n * n

    def calculate(self, a, b):
        result = self.add(a, b)
        return self.square(result)


c = Calculator()

print(c.calculate(2, 3))