from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass

    def display_amount(self):
        print("Amount: 1000")


class UPI(Payment):

    def pay(self):
        print("Payment done using UPI")


p = UPI()
p.pay()
p.display_amount()