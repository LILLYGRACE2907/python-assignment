m1 = int(input("Enter marks in subject 1: "))
m2 = int(input("Enter marks in subject 2: "))
m3 = int(input("Enter marks in subject 3: "))

total = m1 + m2 + m3
average = total / 3
percentage = total / 300 * 100

print("Total =", total)
print("Average =", average)
print("Percentage =", percentage)

if m1 >= 35 and m2 >= 35 and m3 >= 35:
    print("Result: PASS")

    if percentage >= 90:
        print("Grade: A")
    elif percentage >= 75:
        print("Grade: B")
    elif percentage >= 60:
        print("Grade: C")
    else:
        print("Grade: D")
else:
    print("Result: FAIL")
    print("Grade: F")