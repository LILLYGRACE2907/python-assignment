class InvalidFileFormatError(Exception):
    pass


class InvalidDataError(Exception):
    pass


class FileManager:

    def read_file(self, filename):

        try:

            if not filename.endswith(".txt"):
                raise InvalidFileFormatError(
                    "Only .txt files are allowed"
                )

            file = open(filename, "r")

            data = file.read()

            if data == "":
                raise InvalidDataError("File contains no data")

            print(data)

            file.close()

        except FileNotFoundError:
            print("File not found")

        except PermissionError:
            print("Permission denied")

        except InvalidFileFormatError as e:
            print(e)

        except InvalidDataError as e:
            print(e)


manager = FileManager()

filename = input("Enter file name: ")

manager.read_file(filename)