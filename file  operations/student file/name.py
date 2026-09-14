file = open("students.txt", "w")

for i in range(3):
    id = input("Enter ID: ")
    name = input("Enter name: ")
    age = input("Enter age: ")
    course = input("Enter course: ")
    marks = input("Enter marks: ")

    file.write(id + "," + name + "," + age + "," + course + "," + marks + "\n")

file.close()