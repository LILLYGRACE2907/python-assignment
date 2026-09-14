try:
    quantity = int(input("Enter quantity: "))

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero")

    print("Quantity:", quantity)

except ValueError as e:
    print(e)