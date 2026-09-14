from abc import ABC, abstractmethod

class Payment(ABC):

    def __init__(self, amount, transaction_id):
        self.amount = amount
        self.transaction_id = transaction_id

    @abstractmethod
    def pay(self):
        pass


class UPI(Payment):

    def pay(self):
        print("Payment through UPI")


class CreditCard(Payment):

    def pay(self):
        print("Payment through Credit Card")


class NetBanking(Payment):

    def pay(self):
        print("Payment through Net Banking")


u = UPI(1000, "TXN101")

print("Amount:", u.amount)
print("Transaction ID:", u.transaction_id)
u.pay()