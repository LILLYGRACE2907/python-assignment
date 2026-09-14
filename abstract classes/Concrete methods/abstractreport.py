from abc import ABC, abstractmethod

class Report(ABC):

    @abstractmethod
    def generate(self):
        pass

    def display_report_info(self):
        print("Report: Student Report")


class StudentReport(Report):

    def generate(self):
        print("Report generated")


r = StudentReport()
r.generate()
r.display_report_info()