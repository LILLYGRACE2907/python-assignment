file = open("numbers.txt", "r")

numbers = []

for line in file:
    numbers.append(int(line))

file.close()

numbers.sort()

output = open("sorted.txt", "w")

for num in numbers:
    output.write(str(num) + "\n")

output.close()