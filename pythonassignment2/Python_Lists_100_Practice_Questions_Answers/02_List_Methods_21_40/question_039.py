# Python Lists – Practice Question 39
# Question: Find the frequency of every element in a list.

numbers = [1, 2, 2, 3, 1, 2, 3]
frequency = {}
for n in numbers:
    frequency[n] = frequency.get(n, 0) + 1
print(frequency)
