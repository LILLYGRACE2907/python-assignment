file = open("data.txt", "r")
output = open("reverse.txt", "w")

for line in file:
    output.write(line.strip()[::-1] + "\n")

file.close()
output.close()