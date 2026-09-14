from abc import ABC, abstractmethod
class notification(ABC):
    @abstractmethod
    def send(self):
        pass 
class emailnotification(notification):
    def send(self):
        print("Sending email notification") 
class smsnotification(notification):
    def send(self):
        print("Sending SMS notification")
emailnotification().send()
smsnotification().send()
                                                               