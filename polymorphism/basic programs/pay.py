class UPIPayment:
    def pay(self):
        print("Payment made using UPI")


class CardPayment:
    def pay(self):
        print("Payment made using Card")


class CashPayment:
    def pay(self):
        print("Payment made using Cash")


payments = [UPIPayment(), CardPayment(), CashPayment()]

for payment in payments:
    payment.pay()