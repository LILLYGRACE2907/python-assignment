file = open("data.txt", "r")

print("Position:", file.tell())

file.read(5)
print("Position:", file.tell())

file.seek(0)
print("Position:", file.tell())

file.close()