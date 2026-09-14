try:
    file = open("abc.txt", "r")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("File not found")