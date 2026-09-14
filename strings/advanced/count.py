sentence = "Python 123 is easy"

words = len(sentence.split())
characters = len(sentence)
digits = 0
vowels = 0
spaces = 0

for ch in sentence:
    if ch.isdigit():
        digits += 1
    if ch.lower() in "aeiou":
        vowels += 1
    if ch == " ":
        spaces += 1

print("Words:", words)
print("Characters:", characters)
print("Digits:", digits)
print("Vowels:", vowels)
print("Spaces:", spaces)