from abc import ABC,abstractmethod
class food(ABC):
    @abstractmethod
    def prepare(self):
        pass
class pizza(food):
    def prepare(self):
        print("Preparing pizza")
class burger(food):
    def prepare(self):
        print("Preparing burger")
pizza().prepare()
burger().prepare()
        
