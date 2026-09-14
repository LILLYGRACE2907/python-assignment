text = input("Enter a string: ")

result = ""

for ch in text:
    if ch not in result:
        result += ch

print("After removing duplicates =", result)