sentence = input("Enter a sentence: ")

words = sentence.split()

result = ""

for word in words:
    result = word + " " + result

print("Reversed order =", result)