numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter index: "))
    print("Value:", numbers[index])

except ValueError:
    print("Please enter a number")

except IndexError:
    print("Invalid index")