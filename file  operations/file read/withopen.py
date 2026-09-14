with open("data.txt", "w") as file:
    file.write("Welcome to Python")

with open("data.txt", "r") as file:
    print(file.read())