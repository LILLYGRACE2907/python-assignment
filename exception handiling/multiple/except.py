try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b)

    numbers = [10, 20, 30]
    index = int(input("Enter list index: "))

    print("List value:", numbers[index])

except ValueError:
    print("Please enter numbers only")

except ZeroDivisionError:
    print("Cannot divide by zero")

except IndexError:
    print("Invalid list index")

except TypeError:
    print("Invalid data type")