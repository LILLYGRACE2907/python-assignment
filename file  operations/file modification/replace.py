file = open("data.txt", "r")

data = file.read()
data = data.replace("Python", "Java")

file.close()

file = open("data.txt", "w")
file.write(data)
file.close()

print("Word replaced")