class InvalidEmailError(Exception):
    pass


try:
    email = input("Enter email: ")

    if "@" not in email:
        raise InvalidEmailError("Invalid email address")

    print("Valid email")

except InvalidEmailError as e:
    print(e)