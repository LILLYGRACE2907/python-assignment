try:
    marks = int(input("Enter marks: "))

    if marks > 100 or marks < 0:
        raise ValueError("Marks must be between 0 and 100")

    print("Marks:", marks)

except ValueError as e:
    print(e)