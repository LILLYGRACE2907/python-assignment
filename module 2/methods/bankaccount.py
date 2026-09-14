class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def display(self):
        print("Balance:", self.balance)


a = BankAccount("Lilly", 10000)

a.deposit(5000)
a.withdraw(3000)
a.display()