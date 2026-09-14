from abc import ABC, abstractmethod

class FileHandler(ABC):

    @abstractmethod
    def read(self):
        pass


class PDFFile(FileHandler):

    def read(self):
        print("Reading PDF file")


class CSVFile(FileHandler):

    def read(self):
        print("Reading CSV file")


class ExcelFile(FileHandler):

    def read(self):
        print("Reading Excel file")


files = [PDFFile(), CSVFile(), ExcelFile()]

for file in files:
    file.read()