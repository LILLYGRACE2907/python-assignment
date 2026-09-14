class InvalidAgeError(Exception):
    pass


try:
    age = int(input("Enter age: "))

    if age < 18:
        raise InvalidAgeError("Age must be 18 or above")

    print("Valid age")

except InvalidAgeError as e:
    print(e)