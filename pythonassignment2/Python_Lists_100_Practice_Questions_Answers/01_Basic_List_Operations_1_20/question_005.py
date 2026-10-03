# Python Lists – Practice Question 5
# Question: Find the smallest number in a list without using min().

numbers = [12, 45, 7, 89, 23]
smallest = numbers[0]
for n in numbers:
    if n < smallest:
        smallest = n
print("Smallest:", smallest)
