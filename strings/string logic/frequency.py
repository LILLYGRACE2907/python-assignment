text = input("Enter a string: ")

for ch in text:
    if ch not in text[:text.index(ch)]:
        print(ch, "=", text.count(ch))