file = open("numbers.txt", "w")

for i in range(1, 21):
    file.write(str(i) + "\n")

file.close()

file = open("numbers.txt", "r")

total = 0

for line in file:
    total += int(line)

print("Total:", total)

file.close()