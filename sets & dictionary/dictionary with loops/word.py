words = {
    "python": "A programming language",
    "class": "A blueprint for objects",
    "object": "An instance of a class",
    "loop": "Used to repeat statements"
}

word = input("Enter a word: ")

if word in words:
    print("Meaning:", words[word])
else:
    print("Word not found")