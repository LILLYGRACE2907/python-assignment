class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance


account = BankAccount(10000)

result = account.deposit(5000)

print("Balance:", result)