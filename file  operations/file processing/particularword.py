file = open("data.txt", "r")

word = input("Enter word: ")

for line in file:
    if word in line:
        print(line.strip())

file.close()