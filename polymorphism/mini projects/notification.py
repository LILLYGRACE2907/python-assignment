class Notification:
    def send(self, message):
        pass


class Email(Notification):
    def send(self, message):
        print("Email:", message)


class SMS(Notification):
    def send(self, message):
        print("SMS:", message)


class WhatsApp(Notification):
    def send(self, message):
        print("WhatsApp:", message)


notifications = [Email(), SMS(), WhatsApp()]

for notification in notifications:
    notification.send("Hello! Your order is confirmed.")