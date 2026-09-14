users = ["lilly", "john", "ravi", "anu"]

username = input("Enter username: ")

if username in users:
    print("Username exists")
else:
    print("Username does not exist")