class UPIPayment:
    def pay(self):
        print("Payment using UPI")


class CardPayment:
    def pay(self):
        print("Payment using Card")


class CashPayment:
    def pay(self):
        print("Payment using Cash")


def process_payment(payment):
    payment.pay()


upi = UPIPayment()
card = CardPayment()
cash = CashPayment()

process_payment(upi)
process_payment(card)
process_payment(cash)