file = open("numbers.txt", "r")
output = open("odd.txt", "w")

for line in file:
    num = int(line)
    if num % 2 != 0:
        output.write(str(num) + "\n")

file.close()
output.close()