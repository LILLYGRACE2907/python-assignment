class Account:
    def calculate_interest(self, amount):
        pass


class SavingsAccount(Account):
    def calculate_interest(self, amount):
        return amount * 0.05


class CurrentAccount(Account):
    def calculate_interest(self, amount):
        return amount * 0.02


class FixedDeposit(Account):
    def calculate_interest(self, amount):
        return amount * 0.07


accounts = [SavingsAccount(), CurrentAccount(), FixedDeposit()]

amount = 100000

for account in accounts:
    print("Interest:", account.calculate_interest(amount))