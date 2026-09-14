#1.eligible for job
age = 25
qualification = "degree"

if age >= 18 and qualification == "degree":
	print("The person is eligible for the job.")
else:
	print("The person is not eligible for the job.")
#2 check whether user name and password
correct_username = "admin"
correct_password = "python123"
username = "admin"
password = "python123"

if username == correct_username and password == correct_password:
	print("Username and password are correct.")
else:
	print("Username or password is incorrect.")
#3 eligible for discount
age = 65
is_member = False

if age >= 60 or is_member:
	print("The user is eligible for a discount.")
else:
	print("The user is not eligible for a discount.")
