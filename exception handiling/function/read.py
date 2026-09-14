def read_file(filename):
    try:
        file = open(filename, "r")
        data = file.read()
        file.close()

        return data

    except FileNotFoundError:
        return "File not found"

    except PermissionError:
        return "Permission denied"


filename = input("Enter file name: ")

print(read_file(filename))