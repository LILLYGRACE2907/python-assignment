text = input("Enter a string: ")

count = 0

for ch in text:
    if ch.isalpha() and ch not in "aeiouAEIOU":
        count += 1

print("Number of consonants =", count)