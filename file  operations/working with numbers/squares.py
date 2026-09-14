file = open("numbers.txt", "r")
output = open("squares.txt", "w")

for line in file:
    num = int(line)
    output.write(str(num * num) + "\n")

file.close()
output.close()