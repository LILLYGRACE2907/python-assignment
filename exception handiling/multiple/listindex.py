numbers = [10, 20, 30, 40]

try:
    index = int(input("Enter index: "))
    print("Value:", numbers[index])

except ValueError:
    print("Index must be a number")

except IndexError:
    print("Index is out of range")

except TypeError:
    print("Invalid index type")

except Exception:
    print("Some other error occurred")