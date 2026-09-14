import csv

file = open("students.csv", "r")

reader = csv.reader(file)
header = next(reader)

rows = list(reader)

file.close()

rows.sort(key=lambda x: int(x[3]), reverse=True)

file = open("sorted_students.csv", "w", newline="")

writer = csv.writer(file)
writer.writerow(header)
writer.writerows(rows)

file.close()