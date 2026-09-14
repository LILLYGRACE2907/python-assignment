try:
    username = input("Enter username: ")

    if username == "":
        raise ValueError("Username cannot be empty")

    print("Username:", username)

except ValueError as e:
    print(e)