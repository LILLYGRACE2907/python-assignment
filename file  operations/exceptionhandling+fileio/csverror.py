import csv

try:
    file = open("students.csv", "r")
    reader = csv.reader(file)

    for row in reader:
        print(row)

    file.close()

except FileNotFoundError:
    print("CSV file not found")

except Exception:
    print("Error reading CSV file")