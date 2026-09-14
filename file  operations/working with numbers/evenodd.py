file = open("numbers.txt", "r")

even = open("even.txt", "w")
odd = open("odd.txt", "w")

for line in file:
    num = int(line)

    if num % 2 == 0:
        even.write(str(num) + "\n")
    else:
        odd.write(str(num) + "\n")

file.close()
even.close()
odd.close()