class InvalidPaymentError(Exception):
    pass


class Payment:
    def pay(self, amount):
        try:
            if amount <= 0:
                raise InvalidPaymentError(
                    "Payment amount must be greater than zero"
                )

            print("Payment successful:", amount)

        except InvalidPaymentError as e:
            print(e)


payment = Payment()

payment.pay(500)
payment.pay(-100)