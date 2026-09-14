while True:

    print("\n1. Create File")
    print("2. Read File")
    print("3. Write File")
    print("4. Append File")
    print("5. Exit")

    choice = input("Enter choice: ")
    filename = input("Enter filename: ")

    try:

        if choice == "1":
            file = open(filename, "w")
            file.close()
            print("File created")

        elif choice == "2":
            file = open(filename, "r")
            print(file.read())
            file.close()

        elif choice == "3":
            data = input("Enter data: ")
            file = open(filename, "w")
            file.write(data)
            file.close()
            print("Data written")

        elif choice == "4":
            data = input("Enter data: ")
            file = open(filename, "a")
            file.write("\n" + data)
            file.close()
            print("Data appended")

        elif choice == "5":
            break

        else:
            print("Invalid choice")

    except FileNotFoundError:
        print("File not found")

    except Exception:
        print("Something went wrong")