sentence = input("Enter a sentence: ")

words = sentence.split()

smallest = words[0]

for word in words:
    if len(word) < len(smallest):
        smallest = word

print("Smallest word =", smallest)