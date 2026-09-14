salary = float(input("Enter monthly salary: "))
age = int(input("Enter age: "))

if salary >= 25000 and age >= 21 and age <= 60:
    print("Eligible for loan")
else:
    print("Not eligible for loan")