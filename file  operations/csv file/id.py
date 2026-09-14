import csv

file = open("students.csv", "r")

reader = csv.reader(file)

for row in reader:
    if row[0] == "102":
        print(row)

file.close()