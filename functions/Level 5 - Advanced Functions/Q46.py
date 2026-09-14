# Question 46
# Create a recursive function to reverse a string.

def reverse_string(text):
    if text == "":
        return ""
    return reverse_string(text[1:]) + text[0]

print(reverse_string("Python"))
