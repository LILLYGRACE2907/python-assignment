try:
    number = int(input("Enter a number: "))

    if number <= 0:
        raise ValueError("Number must be positive")

    print("Positive number:", number)

except ValueError as e:
    print(e)