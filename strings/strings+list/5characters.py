sentence = "Python programming is very interesting"
words = sentence.split()

result = [word for word in words if len(word) > 5]

print(result)