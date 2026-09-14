try:
    file = open("data.txt", "r")
    print(file.read())
    file.close()

except PermissionError:
    print("Permission denied")