# Python Lists – Practice Question 91
# Question: Separate even and odd numbers while maintaining their original order.

numbers = [3, 2, 5, 8, 7, 4]
even = [n for n in numbers if n % 2 == 0]
odd = [n for n in numbers if n % 2 != 0]
print("Even:", even)
print("Odd:", odd)
