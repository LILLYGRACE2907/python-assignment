try:
    password = input("Enter password: ")

    if len(password) < 8:
        raise ValueError("Password must contain at least 8 characters")

    print("Password accepted")

except ValueError as e:
    print(e)