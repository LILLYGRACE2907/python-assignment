def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Result:", divide(a, b))