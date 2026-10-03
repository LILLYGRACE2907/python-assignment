# Python Lists – Practice Question 4
# Question: Find the largest number in a list without using max().

numbers = [12, 45, 7, 89, 23]
largest = numbers[0]
for n in numbers:
    if n > largest:
        largest = n
print("Largest:", largest)
