class InsufficientBalanceError(Exception):
    pass


try:
    balance = 10000
    amount = int(input("Enter withdrawal amount: "))

    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance")

    balance = balance - amount

    print("Withdrawal successful")
    print("Balance:", balance)

except InsufficientBalanceError as e:
    print(e)