import csv

file = open("students.csv", "r")

reader = csv.reader(file)
next(reader)

topper = None

for row in reader:
    if topper is None or int(row[3]) > int(topper[3]):
        topper = row

print("Topper:", topper)

file.close()