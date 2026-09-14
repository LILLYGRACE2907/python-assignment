file = open("data.txt", "r")

data = file.read()
count = 0

for ch in data:
    if ch.isdigit():
        count += 1

print("Digits:", count)

file.close()