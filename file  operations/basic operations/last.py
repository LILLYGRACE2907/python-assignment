file = open("students.txt", "r")

lines = file.readlines()

for line in lines[-5:]:
    print(line.strip())

file.close()