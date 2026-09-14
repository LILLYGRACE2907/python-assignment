file = open("students.txt", "a")

name = input("Enter student name: ")
age = input("Enter age: ")
course = input("Enter course: ")

file.write("Name: " + name + "\n")
file.write("Age: " + age + "\n")
file.write("Course: " + course + "\n")
file.write("----------------\n")

file.close()

print("Student details added successfully")