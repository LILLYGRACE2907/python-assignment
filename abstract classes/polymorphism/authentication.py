from abc import ABC, abstractmethod

class Authentication(ABC):

    @abstractmethod
    def login(self):
        pass


class PasswordAuth(Authentication):

    def login(self):
        print("Login using Password")


class OTPAuth(Authentication):

    def login(self):
        print("Login using OTP")


class FingerprintAuth(Authentication):

    def login(self):
        print("Login using Fingerprint")


methods = [
    PasswordAuth(),
    OTPAuth(),
    FingerprintAuth()
]

for method in methods:
    method.login()