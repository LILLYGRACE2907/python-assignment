file = open("data.txt", "r")

data = file.read()

file.close()

file = open("lowercase.txt", "w")
file.write(data.lower())
file.close()