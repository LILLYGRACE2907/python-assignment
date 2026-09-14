file = open("data.txt", "r")

ch = input("Enter character: ")

for line in file:
    if line.startswith(ch):
        print(line.strip())

file.close()