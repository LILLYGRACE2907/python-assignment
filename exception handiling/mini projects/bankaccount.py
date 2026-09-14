class InvalidAccountError(Exception):
    pass


class InvalidAmountError(Exception):
    pass


class InsufficientBalanceError(Exception):
    pass


class BankAccount:
    def __init__(self, account_no, name, balance):
        self.account_no = account_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Amount must be greater than zero")

        self.balance += amount
        print("Amount deposited")

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Invalid withdrawal amount")

        if amount > self.balance:
            raise InsufficientBalanceError("Insufficient balance")

        self.balance -= amount
        print("Amount withdrawn")

    def display(self):
        print("Account:", self.account_no)
        print("Name:", self.name)
        print("Balance:", self.balance)


accounts = [
    BankAccount(101, "Lilly", 10000),
    BankAccount(102, "Ravi", 5000)
]


def find_account(account_no):
    for account in accounts:
        if account.account_no == account_no:
            return account

    raise InvalidAccountError("Invalid account number")


try:
    number = int(input("Enter account number: "))
    account = find_account(number)

    amount = float(input("Enter withdrawal amount: "))
    account.withdraw(amount)

    account.display()

except InvalidAccountError as e:
    print(e)

except InvalidAmountError as e:
    print(e)

except InsufficientBalanceError as e:
    print(e)

except ValueError:
    print("Please enter valid numbers")