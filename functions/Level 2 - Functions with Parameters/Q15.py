# Question 15
# Create a function that accepts a number and checks whether it is prime.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print("Prime" if is_prime(17) else "Not Prime")
