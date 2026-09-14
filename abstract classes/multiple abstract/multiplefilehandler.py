from abc import ABC, abstractmethod

class FileHandler(ABC):

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass


class PDFFile(FileHandler):

    def read(self):
        print("Reading PDF file")

    def write(self):
        print("Writing PDF file")


class CSVFile(FileHandler):

    def read(self):
        print("Reading CSV file")

    def write(self):
        print("Writing CSV file")


class ExcelFile(FileHandler):

    def read(self):
        print("Reading Excel file")

    def write(self):
        print("Writing Excel file")


p = PDFFile()
p.read()
p.write()

c = CSVFile()
c.read()
c.write()

e = ExcelFile()
e.read()
e.write()