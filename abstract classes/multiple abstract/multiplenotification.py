from abc import ABC, abstractmethod

class Notification(ABC):

    @abstractmethod
    def send(self):
        pass

    @abstractmethod
    def schedule(self):
        pass


class Email(Notification):

    def send(self):
        print("Email sent")

    def schedule(self):
        print("Email scheduled")


class SMS(Notification):

    def send(self):
        print("SMS sent")

    def schedule(self):
        print("SMS scheduled")


class WhatsApp(Notification):

    def send(self):
        print("WhatsApp message sent")

    def schedule(self):
        print("WhatsApp message scheduled")


e = Email()
e.send()
e.schedule()

s = SMS()
s.send()
s.schedule()

w = WhatsApp()
w.send()
w.schedule()