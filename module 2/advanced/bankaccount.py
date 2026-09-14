class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")


account = BankAccount(10000)

account.withdraw(3000)
account.withdraw(8000)

print("Balance:", account.balance)