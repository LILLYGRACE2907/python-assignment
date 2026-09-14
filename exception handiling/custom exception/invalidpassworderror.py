class InvalidPasswordError(Exception):
    pass


try:
    password = input("Enter password: ")

    if len(password) < 8:
        raise InvalidPasswordError("Password must have at least 8 characters")

    print("Password accepted")

except InvalidPasswordError as e:
    print(e)