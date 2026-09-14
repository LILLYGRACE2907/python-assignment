from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass


class UPI(Payment):
    def pay(self):
        print("Payment using UPI")


class Card(Payment):
    def pay(self):
        print("Payment using Card")


class NetBanking(Payment):
    def pay(self):
        print("Payment using Net Banking")


u = UPI()
c = Card()
n = NetBanking()

u.pay()
c.pay()
n.pay()