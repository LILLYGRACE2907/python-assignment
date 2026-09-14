password = input("Enter password: ")

if len(password) < 8:
    print("Weak Password")
elif password.isalpha() or password.isdigit():
    print("Medium Password")
else:
    print("Strong Password")