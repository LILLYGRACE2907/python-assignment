class InvalidUsernameError(Exception):
    pass


class WeakPasswordError(Exception):
    pass


class DuplicateUsernameError(Exception):
    pass


class InvalidLoginError(Exception):
    pass


class LoginSystem:
    def __init__(self):
        self.users = {}

    def register(self, username, password):

        if username == "":
            raise InvalidUsernameError("Username cannot be empty")

        if len(password) < 8:
            raise WeakPasswordError(
                "Password must contain at least 8 characters"
            )

        if username in self.users:
            raise DuplicateUsernameError("Username already exists")

        self.users[username] = password

        print("Registration successful")

    def login(self, username, password):

        if username not in self.users:
            raise InvalidLoginError("Invalid username or password")

        if self.users[username] != password:
            raise InvalidLoginError("Invalid username or password")

        print("Login successful")


system = LoginSystem()

try:
    system.register("lilly", "12345678")
    system.login("lilly", "12345678")

except InvalidUsernameError as e:
    print(e)

except WeakPasswordError as e:
    print(e)

except DuplicateUsernameError as e:
    print(e)

except InvalidLoginError as e:
    print(e)