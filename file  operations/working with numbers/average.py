file = open("numbers.txt", "r")

numbers = []

for line in file:
    numbers.append(int(line))

average = sum(numbers) / len(numbers)

print("Average:", average)

file.close()