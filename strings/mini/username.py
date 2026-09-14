username = input("Enter username: ")

if len(username) < 5:
    print("Username must contain at least 5 characters")
elif not username.isalnum():
    print("Username should contain only letters and numbers")
else:
    print("Valid Username")