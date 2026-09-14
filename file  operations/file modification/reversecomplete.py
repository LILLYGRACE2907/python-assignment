file = open("data.txt", "r")

data = file.read()

file.close()

output = open("reverse.txt", "w")
output.write(data[::-1])
output.close()