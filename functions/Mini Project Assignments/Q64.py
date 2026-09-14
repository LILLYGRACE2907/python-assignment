# Question 64
# Create a Banking System using Functions with deposit, withdrawal, balance checking, and transaction history.

balance = 0
history = []

def deposit(amount):
    global balance
    balance += amount
    history.append("Deposited " + str(amount))

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        history.append("Withdrawn " + str(amount))
    else:
        print("Insufficient balance")

def show_balance():
    print("Balance:", balance)

def show_history():
    for item in history:
        print(item)

while True:
    print("\n1.Deposit 2.Withdraw 3.Balance 4.History 5.Exit")
    choice = input("Choice: ")
    if choice == "1": deposit(float(input("Amount: ")))
    elif choice == "2": withdraw(float(input("Amount: ")))
    elif choice == "3": show_balance()
    elif choice == "4": show_history()
    elif choice == "5": break
    else: print("Invalid choice")
