sentence = input("Enter a sentence: ")

words = sentence.split()
result = ""

for word in words:
    reverse = ""

    for ch in word:
        reverse = ch + reverse

    result += reverse + " "

print("Result =", result)