sentence = "python is easy python is powerful"
words = sentence.split()

result = list(dict.fromkeys(words))

print(' '.join(result))