file = open("numbers.txt", "r")

numbers = []

for line in file:
    numbers.append(int(line))

print("Smallest:", min(numbers))

file.close()