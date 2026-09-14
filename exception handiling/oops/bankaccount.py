class InsufficientBalanceError(Exception):
    pass


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        try:
            if amount > self.balance:
                raise InsufficientBalanceError("Insufficient balance")

            self.balance = self.balance - amount
            print("Withdrawal successful")
            print("Balance:", self.balance)

        except InsufficientBalanceError as e:
            print(e)


account = BankAccount(10000)

account.withdraw(3000)
account.withdraw(8000)