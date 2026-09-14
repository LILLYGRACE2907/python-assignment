s = "programming"

duplicates = []

for ch in s:
    if s.count(ch) > 1 and ch not in duplicates:
        duplicates.append(ch)

print(duplicates)