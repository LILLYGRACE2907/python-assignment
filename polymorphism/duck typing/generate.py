class ExcelReport:
    def generate(self):
        print("Excel report generated")


class PDFReport:
    def generate(self):
        print("PDF report generated")


def generate_report(report):
    report.generate()


excel = ExcelReport()
pdf = PDFReport()

generate_report(excel)
generate_report(pdf)