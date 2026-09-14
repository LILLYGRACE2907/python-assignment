file = open("data.txt", "w")

lines = ["Python\n", "Java\n", "C\n", "HTML\n"]
file.writelines(lines)

file.close()