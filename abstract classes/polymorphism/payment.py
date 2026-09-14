from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass


class UPI(Payment):

    def pay(self):
        print("Payment using UPI")


class CreditCard(Payment):

    def pay(self):
        print("Payment using Credit Card")


class NetBanking(Payment):

    def pay(self):
        print("Payment using Net Banking")


payments = [UPI(), CreditCard(), NetBanking()]

for payment in payments:
    payment.pay()