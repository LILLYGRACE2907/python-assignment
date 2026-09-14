class GoogleLogin:
    def login(self):
        print("Login using Google")


class FacebookLogin:
    def login(self):
        print("Login using Facebook")


class EmailLogin:
    def login(self):
        print("Login using Email")


def authenticate_user(user):
    user.login()


google = GoogleLogin()
facebook = FacebookLogin()
email = EmailLogin()

authenticate_user(google)
authenticate_user(facebook)
authenticate_user(email)