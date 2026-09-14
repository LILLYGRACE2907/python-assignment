class File:
    def read(self):
        pass

    def write(self):
        pass


class PDF(File):
    def read(self):
        print("Reading PDF file")

    def write(self):
        print("Writing PDF file")


class Excel(File):
    def read(self):
        print("Reading Excel file")

    def write(self):
        print("Writing Excel file")


class Word(File):
    def read(self):
        print("Reading Word file")

    def write(self):
        print("Writing Word file")


class CSV(File):
    def read(self):
        print("Reading CSV file")

    def write(self):
        print("Writing CSV file")


files = [PDF(), Excel(), Word(), CSV()]

for file in files:
    file.read()
    file.write()