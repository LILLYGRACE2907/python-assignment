s = "programming"

unique = []

for ch in s:
    if s.count(ch) == 1:
        unique.append(ch)

print(unique)