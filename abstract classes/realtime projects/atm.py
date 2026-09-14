from abc import ABC, abstractmethod

class ATM(ABC):

    @abstractmethod
    def withdraw(self):
        pass

    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def balance(self):
        pass


class SBI(ATM):

    def withdraw(self):
        print("Withdraw money")

    def deposit(self):
        print("Deposit money")

    def balance(self):
        print("Balance: 10000")


a = SBI()

a.withdraw()
a.deposit()
a.balance()