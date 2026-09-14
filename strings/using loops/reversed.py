text = input("Enter a string: ")

result = ""

for ch in text:
    result = ch + result

print("Reversed string =", result)