import csv

file = open("students.csv", "r")
rows = list(csv.reader(file))
file.close()

for row in rows:
    if row[0] == "102":
        row[3] = "95"

file = open("students.csv", "w", newline="")
writer = csv.writer(file)
writer.writerows(rows)
file.close()