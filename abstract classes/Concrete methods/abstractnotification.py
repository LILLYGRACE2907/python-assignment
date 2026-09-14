from abc import ABC, abstractmethod

class Notification(ABC):

    @abstractmethod
    def send(self):
        pass

    def display_message(self):
        print("Message: Hello!")


class Email(Notification):

    def send(self):
        print("Email sent")


n = Email()
n.send()
n.display_message()