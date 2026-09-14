def get_element(numbers, index):
    try:
        return numbers[index]

    except IndexError:
        return "Invalid index"


numbers = [10, 20, 30, 40]

index = int(input("Enter index: "))

print("Value:", get_element(numbers, index))