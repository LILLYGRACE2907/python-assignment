class InvalidPINError(Exception):
    pass


class InsufficientBalanceError(Exception):
    pass


class InvalidAmountError(Exception):
    pass


class InvalidAccountError(Exception):
    pass


class ATM:
    def __init__(self, account_no, pin, balance):
        self.account_no = account_no
        self.pin = pin
        self.balance = balance

    def withdraw(self, pin, amount):

        if pin != self.pin:
            raise InvalidPINError("Invalid PIN")

        if amount <= 0:
            raise InvalidAmountError("Invalid withdrawal amount")

        if amount > self.balance:
            raise InsufficientBalanceError("Insufficient balance")

        self.balance -= amount

        print("Withdrawal successful")
        print("Balance:", self.balance)


atm = ATM(101, 1234, 10000)

try:
    account = int(input("Enter account number: "))

    if account != atm.account_no:
        raise InvalidAccountError("Invalid account")

    pin = int(input("Enter PIN: "))
    amount = float(input("Enter amount: "))

    atm.withdraw(pin, amount)

except InvalidAccountError as e:
    print(e)

except InvalidPINError as e:
    print(e)

except InvalidAmountError as e:
    print(e)

except InsufficientBalanceError as e:
    print(e)

except ValueError:
    print("Enter valid input")