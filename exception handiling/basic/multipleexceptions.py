try:
    a = int(input("Enter number: "))
    b = int(input("Enter number: "))

    result = a / b

    print("Result:", result)

except ValueError:
    print("Please enter numbers only")

except ZeroDivisionError:
    print("Cannot divide by zero")