text = input("Enter a string: ")

found = False

for ch in text:
    if text.count(ch) > 1:
        print("First repeated character =", ch)
        found = True
        break

if found == False:
    print("No repeated character")