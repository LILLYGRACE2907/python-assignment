# Question 27
# Create a function that accepts a string and checks whether it is a palindrome.

def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

print("Palindrome" if is_palindrome("madam") else "Not Palindrome")
