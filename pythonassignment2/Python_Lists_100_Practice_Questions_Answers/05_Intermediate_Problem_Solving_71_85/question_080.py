# Python Lists – Practice Question 80
# Question: Find the first non-repeating element in a list.

numbers = [4, 5, 1, 2, 1, 4, 5, 3]
for n in numbers:
    if numbers.count(n) == 1:
        print("First non-repeating:", n)
        break
