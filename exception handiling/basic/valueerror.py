try:
    text = "hello"

    number = int(text)

    print(number)

except ValueError:
    print("String cannot be converted into integer")