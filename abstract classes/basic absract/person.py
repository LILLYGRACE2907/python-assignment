from abc import ABC ,abstractmethod
class person(ABC):
    @abstractmethod
    def role(self):
        pass
class student(person):
    def role(self):
      print("I am a student")
class teacher(person):
    def role(self):
      print("I am a teacher")
student().role()
teacher().role()                