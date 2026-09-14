class TextFile:
    def read(self):
        print("Reading text file")


class PDFFile:
    def read(self):
        print("Reading PDF file")


class ExcelFile:
    def read(self):
        print("Reading Excel file")


def read_file(file):
    file.read()


text = TextFile()
pdf = PDFFile()
excel = ExcelFile()

read_file(text)
read_file(pdf)
read_file(excel)