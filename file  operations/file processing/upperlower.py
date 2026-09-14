file = open("data.txt", "r")

data = file.read()

upper = 0
lower = 0

for ch in data:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

print("Uppercase:", upper)
print("Lowercase:", lower)

file.close()