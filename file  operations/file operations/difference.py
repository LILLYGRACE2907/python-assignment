# r mode - Read
file = open("data.txt", "r")
print(file.read())
file.close()


# w mode - Write
# It creates a new file or overwrites old content
file = open("data.txt", "w")
file.write("New Data")
file.close()


# a mode - Append
# It adds data at the end
file = open("data.txt", "a")
file.write("\nAdditional Data")
file.close()