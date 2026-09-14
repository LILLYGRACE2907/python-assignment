class InvalidPasswordError(Exception):
    pass


def validate_password(password):
    try:
        if len(password) < 8:
            raise InvalidPasswordError(
                "Password must contain at least 8 characters"
            )

        return "Password is valid"

    except InvalidPasswordError as e:
        return e


password = input("Enter password: ")

print(validate_password(password))