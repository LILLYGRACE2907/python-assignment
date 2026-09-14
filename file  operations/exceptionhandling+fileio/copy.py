try:
    source = open("data.txt", "r")
    destination = open("copy.txt", "w")

    destination.write(source.read())

    source.close()
    destination.close()

    print("File copied successfully")

except FileNotFoundError:
    print("Source file not found")

except Exception:
    print("Error copying file")