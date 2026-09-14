sentence = "python is easy and python is powerful"
words = sentence.split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)