# Question 10
# Create a function called is_positive() that accepts a number and checks whether it is positive, negative, or zero.

def is_positive(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    return "Zero"

print(is_positive(-5))
