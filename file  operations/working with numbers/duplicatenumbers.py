file = open("numbers.txt", "r")

numbers = []

for line in file:
    numbers.append(int(line))

file.close()

for num in set(numbers):
    if numbers.count(num) > 1:
        print("Duplicate:", num)