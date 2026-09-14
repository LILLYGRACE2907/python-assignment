def grade(marks):
    try:
        if marks < 0 or marks > 100:
            raise ValueError("Invalid marks")

        if marks >= 90:
            return "A"
        elif marks >= 75:
            return "B"
        elif marks >= 60:
            return "C"
        elif marks >= 40:
            return "D"
        else:
            return "Fail"

    except ValueError as e:
        return e


marks = int(input("Enter marks: "))

print("Grade:", grade(marks))