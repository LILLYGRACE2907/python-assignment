class BankAccount:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def display(self):
        print("Account Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)
        print()


a1 = BankAccount("Lilly", 1001, 50000)
a2 = BankAccount("Anu", 1002, 35000)

a1.display()
a2.display()