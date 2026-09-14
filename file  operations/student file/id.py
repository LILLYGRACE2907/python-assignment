file = open("students.txt", "r")

student_id = input("Enter ID: ")

for line in file:
    data = line.strip().split(",")

    if data[0] == student_id:
        print(line.strip())

file.close()