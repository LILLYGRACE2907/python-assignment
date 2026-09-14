file = open("data.txt", "r")

data = file.read()
count = 0

for ch in data:
    if ch.lower() in "aeiou":
        count += 1

print("Vowels:", count)

file.close()