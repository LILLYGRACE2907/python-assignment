# Question 9
# Create a BankAccount class and derive SavingsAccount and CurrentAccount classes.

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

class SavingsAccount(BankAccount):
    def show(self):
        print("Savings balance:", self.balance)

class CurrentAccount(BankAccount):
    def show(self):
        print("Current balance:", self.balance)

SavingsAccount(5000).show()
CurrentAccount(8000).show()
