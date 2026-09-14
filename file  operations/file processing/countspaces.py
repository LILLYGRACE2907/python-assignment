file = open("data.txt", "r")

data = file.read()
count = 0

for ch in data:
    if ch == " ":
        count += 1

print("Spaces:", count)

file.close()