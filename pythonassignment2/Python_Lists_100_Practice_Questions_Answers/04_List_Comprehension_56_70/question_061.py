# Python Lists – Practice Question 61
# Question: Generate numbers divisible by both 3 and 5.

numbers = [n for n in range(1, 101) if n % 3 == 0 and n % 5 == 0]
print(numbers)
