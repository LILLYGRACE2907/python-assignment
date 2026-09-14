# Question 58
# Create a function that accepts a string and returns a dictionary containing the frequency of each character.

def character_frequency(text):
    frequency = {}
    for ch in text:
        frequency[ch] = frequency.get(ch, 0) + 1
    return frequency

print(character_frequency("hello"))
