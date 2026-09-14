file = open("data.txt", "r")

print("Position:", file.tell())

file.read(5)

print("Position:", file.tell())

file.close()