while True:
    print("\n--- STRING MENU ---")
    print("1. Reverse")
    print("2. Palindrome")
    print("3. Vowel Count")
    print("4. Word Count")
    print("5. Character Frequency")
    print("6. Uppercase")
    print("7. Lowercase")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 8:
        print("Program ended")
        break

    text = input("Enter a string: ")

    if choice == 1:
        print("Reverse:", text[::-1])

    elif choice == 2:
        if text == text[::-1]:
            print("Palindrome")
        else:
            print("Not a Palindrome")

    elif choice == 3:
        count = 0
        for ch in text:
            if ch.lower() in "aeiou":
                count += 1
        print("Vowel Count:", count)

    elif choice == 4:
        print("Word Count:", len(text.split()))

    elif choice == 5:
        frequency = {}
        for ch in text:
            frequency[ch] = frequency.get(ch, 0) + 1
        print(frequency)

    elif choice == 6:
        print("Uppercase:", text.upper())

    elif choice == 7:
        print("Lowercase:", text.lower())

    else:
        print("Invalid Choice")