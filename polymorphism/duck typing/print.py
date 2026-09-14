class Printer:
    def print(self):
        print("Printing document")


class PDFPrinter:
    def print(self):
        print("Printing PDF document")


def do_print(device):
    device.print()


p = Printer()
pdf = PDFPrinter()

do_print(p)
do_print(pdf)