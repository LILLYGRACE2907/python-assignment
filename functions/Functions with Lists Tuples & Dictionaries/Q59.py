# Question 59
# Create a function that accepts a sentence and returns a dictionary containing the frequency of each word.

def word_frequency(sentence):
    frequency = {}
    for word in sentence.lower().split():
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

print(word_frequency("python is easy and python is useful"))
