file = open("numbers.txt", "r")
output = open("cubes.txt", "w")

for line in file:
    num = int(line)
    output.write(str(num * num * num) + "\n")

file.close()
output.close()