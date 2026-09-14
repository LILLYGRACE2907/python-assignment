file = open("students.txt", "r")

total = 0
count = 0

for line in file:
    data = line.strip().split(",")
    total += int(data[4])
    count += 1

print("Average:", total / count)

file.close()