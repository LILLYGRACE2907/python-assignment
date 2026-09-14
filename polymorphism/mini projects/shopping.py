class Payment:
    def pay(self, amount):
        pass


class UPI(Payment):
    def pay(self, amount):
        print("Paid ₹", amount, "using UPI")


class Card(Payment):
    def pay(self, amount):
        print("Paid ₹", amount, "using Card")


class NetBanking(Payment):
    def pay(self, amount):
        print("Paid ₹", amount, "using Net Banking")


payments = [UPI(), Card(), NetBanking()]

for payment in payments:
    payment.pay(2500)