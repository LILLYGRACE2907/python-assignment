s = "I have 2 books and 5 pens"

numbers = []

for word in s.split():
    if word.isdigit():
        numbers.append(word)

print(numbers)