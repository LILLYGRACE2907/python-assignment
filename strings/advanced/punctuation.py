import string

s = "Hello, Python! How are you?"

result = ""

for ch in s:
    if ch not in string.punctuation:
        result += ch

print(result)