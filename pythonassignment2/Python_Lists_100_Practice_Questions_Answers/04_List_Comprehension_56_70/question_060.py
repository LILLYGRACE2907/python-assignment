# Python Lists – Practice Question 60
# Question: Generate only odd numbers from 1 to 100.

odd = [n for n in range(1, 101) if n % 2 != 0]
print(odd)
