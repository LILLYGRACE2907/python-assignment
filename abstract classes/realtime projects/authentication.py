from abc import ABC, abstractmethod

class Authentication(ABC):

    @abstractmethod
    def login(self):
        pass


class Password(Authentication):

    def login(self):
        print("Login using Password")


class OTP(Authentication):

    def login(self):
        print("Login using OTP")


class GoogleLogin(Authentication):

    def login(self):
        print("Login using Google")


class Biometric(Authentication):

    def login(self):
        print("Login using Biometric")


Password().login()
OTP().login()
GoogleLogin().login()
Biometric().login()