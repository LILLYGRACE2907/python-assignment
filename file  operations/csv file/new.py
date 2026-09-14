import csv

file = open("students.csv", "a", newline="")

writer = csv.writer(file)

writer.writerow([103, "Anjali", "Python", 78])

file.close()