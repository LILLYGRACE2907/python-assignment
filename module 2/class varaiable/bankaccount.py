class BankAccount:
    bank_name = "SBI"

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def display(self):
        print("Account Holder:", self.account_holder)
        print("Balance:", self.balance)
        print("Bank:", BankAccount.bank_name)


a1 = BankAccount("Lilly", 50000)
a2 = BankAccount("Anu", 30000)
a3 = BankAccount("Ravi", 40000)

a1.display()
a2.display()
a3.display()