from abc import ABC, abstractmethod

class BankAccount(ABC):

    @abstractmethod
    def calculate_interest(self):
        pass

    def display_balance(self):
        print("Balance: 10000")


class SavingsAccount(BankAccount):

    def calculate_interest(self):
        print("Interest: 500")


b = SavingsAccount()
b.calculate_interest()
b.display_balance()