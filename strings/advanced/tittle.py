sentence = "python is easy to learn"

words = sentence.split()

result = []

for word in words:
    result.append(word[0].upper() + word[1:])

print(' '.join(result))