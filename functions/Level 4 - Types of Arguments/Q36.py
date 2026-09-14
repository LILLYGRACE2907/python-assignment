# Question 36
# Create a function using **kwargs to display employee information.

def employee_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

employee_info(name="Lilly", department="IT", salary=25000)
