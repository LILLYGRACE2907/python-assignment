from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class dog(Animal):
    def sound(self):
        print("bark")
class cat(Animal):
    def sound(self):
        print("meow")
d=dog()
c=cat()
d.sound()
c.sound()        
