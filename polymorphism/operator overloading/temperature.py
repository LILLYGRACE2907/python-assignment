class Temperature:
    def __init__(self, degree):
        self.degree = degree

    def __gt__(self, other):
        return self.degree > other.degree


t1 = Temperature(35)
t2 = Temperature(30)

if t1 > t2:
    print("Temperature 1 is higher")
else:
    print("Temperature 2 is higher")