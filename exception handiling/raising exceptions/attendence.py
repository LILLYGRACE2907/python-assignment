try:
    attendance = float(input("Enter attendance percentage: "))

    if attendance < 75:
        raise ValueError("Attendance is below 75%")

    print("Attendance is sufficient")

except ValueError as e:
    print(e)