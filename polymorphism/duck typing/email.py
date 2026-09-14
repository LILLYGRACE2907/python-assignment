class EmailService:
    def send(self):
        print("Email sent")


class SMSService:
    def send(self):
        print("SMS sent")


def send_message(service):
    service.send()


email = EmailService()
sms = SMSService()

send_message(email)
send_message(sms)