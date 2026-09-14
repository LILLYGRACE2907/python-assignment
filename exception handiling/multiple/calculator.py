try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    operation = input("Enter operation (+, -, *, /): ")

    if operation == "+":
        print("Result:", a + b)

    elif operation == "-":
        print("Result:", a - b)

    elif operation == "*":
        print("Result:", a * b)

    elif operation == "/":
        print("Result:", a / b)

    else:
        print("Invalid operation")

except ValueError:
    print("Please enter valid numbers")

except ZeroDivisionError:
    print("Cannot divide by zero")

except TypeError:
    print("Invalid data type")