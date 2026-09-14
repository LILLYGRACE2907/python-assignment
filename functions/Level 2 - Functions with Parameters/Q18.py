# Question 18
# Create a function that accepts a string and counts the number of vowels.

def count_vowels(text):
    count = 0
    for ch in text.lower():
        if ch in "aeiou":
            count += 1
    return count

print("Vowels =", count_vowels("Hello Python"))
