# Question 45
# Create a recursive function to calculate the sum of numbers from 1 to n.

def recursive_sum(n):
    if n == 0:
        return 0
    return n + recursive_sum(n - 1)

print("Sum =", recursive_sum(5))
