import csv

file = open("students.csv", "r")
rows = list(csv.reader(file))
file.close()

rows = [row for row in rows if row[0] != "102"]

file = open("students.csv", "w", newline="")
writer = csv.writer(file)
writer.writerows(rows)
file.close()