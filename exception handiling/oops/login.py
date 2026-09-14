class InvalidUsernameError(Exception):
    pass


class InvalidPasswordError(Exception):
    pass


class LoginSystem:
    def login(self, username, password):
        try:
            if username != "admin":
                raise InvalidUsernameError("Invalid username")

            if password != "1234":
                raise InvalidPasswordError("Invalid password")

            print("Login successful")

        except InvalidUsernameError as e:
            print(e)

        except InvalidPasswordError as e:
            print(e)


login = LoginSystem()

login.login("admin", "1234")
login.login("user", "1234")
login.login("admin", "1111")