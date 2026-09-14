file = open("data.txt", "r")

data = file.read()
words = data.split()

print("Total words:", len(words))

file.close()