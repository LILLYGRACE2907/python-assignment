# Question 40
# Create a function that accepts variable numbers of arguments and separates even and odd numbers.

def separate(*args):
    even = []
    odd = []
    for n in args:
        if n % 2 == 0:
            even.append(n)
        else:
            odd.append(n)
    return even, odd

even, odd = separate(1, 2, 3, 4, 5, 6)
print("Even:", even)
print("Odd:", odd)
