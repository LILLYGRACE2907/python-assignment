class EmailNotification:
    def send(self):
        print("Email notification sent")


class SMSNotification:
    def send(self):
        print("SMS notification sent")


class PushNotification:
    def send(self):
        print("Push notification sent")


def send_notification(notification):
    notification.send()


email = EmailNotification()
sms = SMSNotification()
push = PushNotification()

send_notification(email)
send_notification(sms)
send_notification(push)