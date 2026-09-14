import csv

file = open("students.csv", "w", newline="")

writer = csv.writer(file)

writer.writerow(["ID", "Name", "Course", "Marks"])
writer.writerow([101, "Rahul", "Python", 85])
writer.writerow([102, "Priya", "Java", 92])

file.close()