def factorial(n):
    try:
        if n < 0:
            raise ValueError("Number cannot be negative")

        result = 1

        for i in range(1, n + 1):
            result = result * i

        return result

    except ValueError as e:
        return e


n = int(input("Enter a number: "))

print("Factorial:", factorial(n))