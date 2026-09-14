sentence = input("Enter a sentence: ")

count = 0
inside_word = False

for ch in sentence:
    if ch != " " and inside_word == False:
        count += 1
        inside_word = True
    elif ch == " ":
        inside_word = False

print("Number of words =", count)