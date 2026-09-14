# Question 16
# Create a function that accepts a number and checks whether it is a palindrome.

def is_palindrome(n):
    text = str(n)
    return text == text[::-1]

print("Palindrome" if is_palindrome(121) else "Not Palindrome")
