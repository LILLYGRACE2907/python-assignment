from abc import ABC, abstractmethod

class Account(ABC):

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    @abstractmethod
    def account_type(self):
        pass


class SavingsAccount(Account):

    def account_type(self):
        print("Account Type: Savings Account")


class CurrentAccount(Account):

    def account_type(self):
        print("Account Type: Current Account")


s = SavingsAccount(10101, 25000)
c = CurrentAccount(20202, 50000)

print("Account Number:", s.account_number)
print("Balance:", s.balance)
s.account_type()

print("Account Number:", c.account_number)
print("Balance:", c.balance)
c.account_type()