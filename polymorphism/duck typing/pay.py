class DebitCard:
    def pay(self):
        print("Payment using Debit Card")


class CreditCard:
    def pay(self):
        print("Payment using Credit Card")


def make_payment(card):
    card.pay()


debit = DebitCard()
credit = CreditCard()

make_payment(debit)
make_payment(credit)