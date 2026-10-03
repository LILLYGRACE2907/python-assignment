# Python Lists – Practice Question 15
# Question: Find the average of numbers in a list.

numbers = [10, 20, 30, 40, 50]
total = 0
count = 0
for n in numbers:
    total += n
    count += 1
average = total / count
print("Average:", average)
