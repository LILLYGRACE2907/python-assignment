file = open("students.txt", "r")

for line in file:
    data = line.strip().split(",")

    if int(data[4]) > 75:
        print(line.strip())

file.close()