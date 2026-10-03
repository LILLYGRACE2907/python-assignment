# Python Lists – Practice Question 83
# Question: Find the element that occurs least frequently.

numbers = [1, 2, 2, 3, 3, 3, 4]
least = numbers[0]
min_count = float("inf")
for n in numbers:
    count = numbers.count(n)
    if count < min_count:
        min_count = count
        least = n
print("Least frequent:", least)
