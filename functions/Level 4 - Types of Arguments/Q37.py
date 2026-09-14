# Question 37
# Create a function using both *args and **kwargs to display student details and marks.

def student_details(*marks, **details):
    print("Student Details:")
    for key, value in details.items():
        print(key, ":", value)
    print("Marks:", marks)

student_details(80, 85, 90, name="Lilly", course="CCN")
