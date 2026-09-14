from abc import ABC, abstractmethod
class employee(ABC):
    @abstractmethod
    def work(self):
        pass
class developer(employee):
    def work(self):
        print("I am a developer, I write code.")    
class tester(employee):
    def work(self):
        print("I am a tester, I test code.")
developer().work()
tester().work()