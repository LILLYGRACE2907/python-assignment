file = open("numbers.txt", "r")

for line in file:
    try:
        num = int(line)
        print(num)
    except ValueError:
        print("Invalid number:", line.strip())

file.close()