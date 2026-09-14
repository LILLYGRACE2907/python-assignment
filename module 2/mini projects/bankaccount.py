class BankAccount:
    def __init__(self, account_no, name, balance):
        self.account_no = account_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Amount deposited")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Amount withdrawn")
        else:
            print("Insufficient balance")

    def check_balance(self):
        print("Balance:", self.balance)

    def display(self):
        print("Account No:", self.account_no)
        print("Name:", self.name)
        print("Balance:", self.balance)


accounts = []


def create_account():
    number = int(input("Enter Account Number: "))
    name = input("Enter Name: ")
    balance = float(input("Enter Initial Balance: "))

    account = BankAccount(number, name, balance)
    accounts.append(account)

    print("Account created")


def find_account(number):
    for account in accounts:
        if account.account_no == number:
            return account

    return None


while True:
    print("\n1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Account Details")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        create_account()

    elif choice == 2:
        number = int(input("Enter Account Number: "))
        account = find_account(number)

        if account:
            amount = float(input("Enter Amount: "))
            account.deposit(amount)
        else:
            print("Account not found")

    elif choice == 3:
        number = int(input("Enter Account Number: "))
        account = find_account(number)

        if account:
            amount = float(input("Enter Amount: "))
            account.withdraw(amount)
        else:
            print("Account not found")

    elif choice == 4:
        number = int(input("Enter Account Number: "))
        account = find_account(number)

        if account:
            account.check_balance()
        else:
            print("Account not found")

    elif choice == 5:
        number = int(input("Enter Account Number: "))
        account = find_account(number)

        if account:
            account.display()
        else:
            print("Account not found")

    elif choice == 6:
        break

    else:
        print("Invalid choice")