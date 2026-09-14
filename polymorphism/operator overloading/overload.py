class Distance:
    def __init__(self, meter):
        self.meter = meter

    def __add__(self, other):
        return Distance(self.meter + other.meter)

    def display(self):
        print("Distance:", self.meter, "meters")


d1 = Distance(10)
d2 = Distance(20)

d3 = d1 + d2
d3.display()