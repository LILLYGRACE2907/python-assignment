from abc import ABC , abstractmethod
class payment(ABC):
    @abstractmethod
    def pay(self):
        pass
class upipayment(payment):
    def pay(self):
        print("Payment done using UPI")
class cardpayment(payment):
    def pay(self):
        print("Payment done using Card")
upipayment().pay()
cardpayment().pay()                     