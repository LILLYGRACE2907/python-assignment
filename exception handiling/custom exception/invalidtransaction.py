class InvalidTransactionError(Exception):
    pass


try:
    amount = int(input("Enter transaction amount: "))

    if amount <= 0:
        raise InvalidTransactionError(
            "Transaction amount must be greater than zero"
        )

    print("Transaction successful")

except InvalidTransactionError as e:
    print(e)