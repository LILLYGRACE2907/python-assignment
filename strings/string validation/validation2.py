#1.check it contains only strings
username = input("Enter a username: ")
if username.isalnum():
	print("Username contains only alphabets and numbers.")
else:
	print("Username contains other characters.")

#2.password
password = input("Enter a password: ")
if any(character.isdigit() for character in password):
	print("Password contains at least one digit.")
else:
	print("Password does not contain a digit.")

#3.containes characters or not
entered_string = input("Enter a string: ")
if entered_string:
	print("The string contains characters.")
else:
	print("The string is empty.")
#4.checks email address
email = input("Enter an email address: ")
if "@" in email and "." in email:
	print("Email contains '@' and '.'.")
else:
	print("Email does not contain both '@' and '.'.")
