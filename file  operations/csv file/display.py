import csv

file = open("students.csv", "r")

reader = csv.reader(file)
next(reader)

for row in reader:
    if int(row[3]) < 40:
        print(row)

file.close()