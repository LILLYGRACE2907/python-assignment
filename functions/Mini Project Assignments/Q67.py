# Question 67
# Create a Number Utility Program using Functions with options for prime checking, palindrome checking, factorial, Fibonacci, even/odd, and Armstrong number checking.

def prime(n):
    if n < 2: return False
    for i in range(2, n):
        if n % i == 0: return False
    return True

def palindrome(n):
    return str(n) == str(n)[::-1]

def factorial(n):
    result = 1
    for i in range(1, n + 1): result *= i
    return result

def fibonacci(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

def even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

def armstrong(n):
    digits = str(n)
    return sum(int(d) ** len(digits) for d in digits) == n

while True:
    print("\n1.Prime 2.Palindrome 3.Factorial 4.Fibonacci 5.Even/Odd 6.Armstrong 7.Exit")
    choice = input("Choice: ")
    if choice == "7": break
    n = int(input("Enter number: "))
    if choice == "1": print(prime(n))
    elif choice == "2": print(palindrome(n))
    elif choice == "3": print(factorial(n))
    elif choice == "4": print(fibonacci(n))
    elif choice == "5": print(even_odd(n))
    elif choice == "6": print(armstrong(n))
    else: print("Invalid choice")
