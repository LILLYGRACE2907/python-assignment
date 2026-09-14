name = input("Enter student name: ")
age = int(input("Enter age: "))
marks = int(input("Enter marks: "))

if age >= 18 and marks >= 50:
    print(name, "is eligible")
else:
    print(name, "is not eligible")