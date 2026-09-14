from abc import ABC, abstractmethod

class Report(ABC):

    @abstractmethod
    def generate(self):
        pass


class PDFReport(Report):

    def generate(self):
        print("PDF report generated")


class ExcelReport(Report):

    def generate(self):
        print("Excel report generated")


class HTMLReport(Report):

    def generate(self):
        print("HTML report generated")


reports = [
    PDFReport(),
    ExcelReport(),
    HTMLReport()
]

for report in reports:
    report.generate()