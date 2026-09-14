class Payment:
    def pay(self):
        print("Making payment")


class UPI(Payment):
    def pay(self):
        print("Payment made using UPI")


class CreditCard(Payment):
    def pay(self):
        print("Payment made using Credit Card")


class NetBanking(Payment):
    def pay(self):
        print("Payment made using Net Banking")


payments = [UPI(), CreditCard(), NetBanking()]

for payment in payments:
    payment.pay()