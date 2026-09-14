from abc import ABC ,abstractmethod
class bankaccount(ABC):
    @abstractmethod
    def calculate_interest(self):
        pass 
class savingsaccount(bankaccount):
    def calculate_interest(self):
        print("Calculating interest for savings account")
class currentaccount(bankaccount):
    def calculate_interest(self):
        print("Calculating interest for current account")
savingsaccount().calculate_interest()
currentaccount().calculate_interest()
                    