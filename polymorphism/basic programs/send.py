class EmailNotification:
    def send(self):
        print("Sending notification through Email")


class SMSNotification:
    def send(self):
        print("Sending notification through SMS")


notifications = [EmailNotification(), SMSNotification()]

for notification in notifications:
    notification.send()