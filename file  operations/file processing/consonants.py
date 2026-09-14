file = open("data.txt", "r")

data = file.read()
count = 0

for ch in data:
    if ch.isalpha() and ch.lower() not in "aeiou":
        count += 1

print("Consonants:", count)

file.close()