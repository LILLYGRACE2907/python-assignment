file = open("data.txt", "r")

data = file.read()
data = " ".join(data.split())

file.close()

file = open("newdata.txt", "w")
file.write(data)
file.close()