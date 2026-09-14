def calculate():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        result = a / b

        print("Result:", result)

    except ValueError:
        print("Please enter numbers only")

    except ZeroDivisionError:
        print("Cannot divide by zero")

    except TypeError:
        print("Invalid data type")


calculate()