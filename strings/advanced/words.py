sentence = "Python programming is powerful and popular"
letter = "p"

words = sentence.split()

result = []

for word in words:
    if word.lower().startswith(letter.lower()):
        result.append(word)

print(result)