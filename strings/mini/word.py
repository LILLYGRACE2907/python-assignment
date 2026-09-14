paragraph = input("Enter a paragraph: ")

words = paragraph.lower().split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

for word, count in frequency.items():
    print(word, ":", count)