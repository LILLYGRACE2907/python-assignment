from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class circle(shape):
    def area(self):
        r=5
        p=3.14
        print("circle area is:",p*r*r)
class rectangle(shape):
    def area(self):
        l=5
        b=6
        print("rectangle area is:",l*b)
circle().area()
rectangle().area()                