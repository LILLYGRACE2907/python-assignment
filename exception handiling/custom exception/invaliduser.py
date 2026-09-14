class InvalidUsernameError(Exception):
    pass


try:
    username = input("Enter username: ")

    if username == "":
        raise InvalidUsernameError("Username cannot be empty")

    print("Username accepted")

except InvalidUsernameError as e:
    print(e)