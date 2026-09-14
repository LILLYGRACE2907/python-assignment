from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass

    @abstractmethod
    def refund(self):
        pass


class UPI(Payment):

    def pay(self):
        print("Payment done using UPI")

    def refund(self):
        print("UPI payment refunded")


class CreditCard(Payment):

    def pay(self):
        print("Payment done using Credit Card")

    def refund(self):
        print("Credit Card payment refunded")


class NetBanking(Payment):

    def pay(self):
        print("Payment done using Net Banking")

    def refund(self):
        print("Net Banking payment refunded")


u = UPI()
u.pay()
u.refund()

c = CreditCard()
c.pay()
c.refund()

n = NetBanking()
n.pay()
n.refund()