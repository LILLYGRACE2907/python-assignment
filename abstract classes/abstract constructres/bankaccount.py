from abc import ABC, abstractmethod

class BankAccount(ABC):

    def __init__(self, holder, account_number):
        self.holder = holder
        self.account_number = account_number

    @abstractmethod
    def calculate_interest(self):
        pass


class SavingsAccount(BankAccount):

    def calculate_interest(self):
        print("Savings Account Interest: 5%")


a = SavingsAccount("Lilly", 12345)

print("Account Holder:", a.holder)
print("Account Number:", a.account_number)
a.calculate_interest()