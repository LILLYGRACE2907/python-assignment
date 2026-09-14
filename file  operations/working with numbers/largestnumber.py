file = open("numbers.txt", "r")

numbers = []

for line in file:
    numbers.append(int(line))

print("Largest:", max(numbers))

file.close()