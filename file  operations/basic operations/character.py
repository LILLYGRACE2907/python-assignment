file = open("sample.txt", "r")

data = file.read()

for character in data:
    print(character)

file.close()