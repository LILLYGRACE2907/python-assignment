text = input("Enter a string: ")

for ch in text:
    if ch.isalpha() and ch not in "aeiouAEIOU":
        print(ch)