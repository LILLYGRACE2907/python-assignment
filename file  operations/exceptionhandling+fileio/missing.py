filename = input("Enter filename: ")

try:
    file = open(filename, "r")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("File does not exist")