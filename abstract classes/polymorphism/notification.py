from abc import ABC, abstractmethod

class Notification(ABC):

    @abstractmethod
    def send(self):
        pass


class Email(Notification):

    def send(self):
        print("Email notification sent")


class SMS(Notification):

    def send(self):
        print("SMS notification sent")


class WhatsApp(Notification):

    def send(self):
        print("WhatsApp notification sent")


notifications = [Email(), SMS(), WhatsApp()]

for notification in notifications:
    notification.send()