try:
    file = open("student.txt", "r")

    print(file.read())

    file.close()

except FileNotFoundError:
    print("File does not exist")