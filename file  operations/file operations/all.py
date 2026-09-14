# Create and write data
file = open("sample.txt", "w")
file.write("Welcome to Python\n")
file.write("File Handling")
file.close()


# Read data
file = open("sample.txt", "r")
print("Existing Data:")
print(file.read())
file.close()


# Append new data
file = open("sample.txt", "a")
file.write("\nThis is new data")
file.close()


# Read updated data
file = open("sample.txt", "r")
print("\nUpdated Data:")
print(file.read())
file.close()