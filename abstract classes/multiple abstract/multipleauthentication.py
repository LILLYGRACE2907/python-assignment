from abc import ABC, abstractmethod

class Authentication(ABC):

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass


class PasswordAuth(Authentication):

    def login(self):
        print("Login using Password")

    def logout(self):
        print("Password user logged out")


class OTPAuth(Authentication):

    def login(self):
        print("Login using OTP")

    def logout(self):
        print("OTP user logged out")


p = PasswordAuth()
p.login()
p.logout()

o = OTPAuth()
o.login()
o.logout()