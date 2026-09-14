try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Sum:", a + b)

except ValueError:
    print("Please enter numbers only")