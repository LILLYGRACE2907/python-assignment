try:
    number = int(input("Enter a number: "))

    if number < 0:
        raise ValueError("Number cannot be negative")

    print("Number:", number)

except ValueError as e:
    print(e)