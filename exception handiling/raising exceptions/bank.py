try:
    balance = 10000
    amount = int(input("Enter withdrawal amount: "))

    if amount > balance:
        raise ValueError("Insufficient balance")

    balance = balance - amount

    print("Withdrawal successful")
    print("Remaining Balance:", balance)

except ValueError as e:
    print(e)