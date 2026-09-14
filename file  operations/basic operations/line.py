file = open("students.txt", "r")

for line in file:
    print(line.strip())

file.close()