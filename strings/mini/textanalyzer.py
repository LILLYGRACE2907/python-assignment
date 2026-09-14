text = input("Enter text: ")

characters = len(text)
words = len(text.split())
vowels = 0
consonants = 0
digits = 0
spaces = 0
special = 0

for ch in text:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
    else:
        special += 1

print("Characters:", characters)
print("Words:", words)
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special Characters:", special)