# Python Lists – Practice Question 69
# Question: Extract vowels from a given string using list comprehension.

text = "programming"
vowels = [ch for ch in text if ch.lower() in "aeiou"]
print(vowels)
