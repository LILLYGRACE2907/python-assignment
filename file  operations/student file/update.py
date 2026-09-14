file = open("students.txt", "r")

lines = file.readlines()
file.close()

student_id = input("Enter ID: ")
new_marks = input("Enter new marks: ")

file = open("students.txt", "w")

for line in lines:
    data = line.strip().split(",")

    if data[0] == student_id:
        data[4] = new_marks

    file.write(",".join(data) + "\n")

file.close()