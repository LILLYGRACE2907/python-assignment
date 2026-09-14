n = int(input("Enter a number: "))

# Positive or Negative
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

# Even or Odd
if n % 2 == 0:
    print("Even")
else:
    print("Odd")

# Divisible by 3 and 5
if n % 3 == 0 and n % 5 == 0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible by both 3 and 5")

# Range
if n >= 1 and n <= 100:
    print("Number is between 1 and 100")
else:
    print("Number is outside the range")