import os

if os.path.exists("data.txt"):
    file = open("data.txt", "r")
    print(file.read())
    file.close()
else:
    print("File does not exist")