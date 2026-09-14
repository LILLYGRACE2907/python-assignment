file = open("data.txt", "r")

lines = file.readlines()
file.close()

output = open("newdata.txt", "w")

seen = set()

for line in lines:
    if line not in seen:
        output.write(line)
        seen.add(line)

output.close()