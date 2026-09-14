def withdraw(balance, amount):
    try:
        if amount > balance:
            raise ValueError("Insufficient balance")

        balance = balance - amount
        return balance

    except ValueError as e:
        return e


balance = 10000
amount = int(input("Enter withdrawal amount: "))

print("Result:", withdraw(balance, amount))