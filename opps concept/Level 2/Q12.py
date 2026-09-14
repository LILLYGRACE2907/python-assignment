# Question 12
# Create a Computer class that HAS-A CPU object.

class CPU:
    def __init__(self, name):
        self.name = name

class Computer:
    def __init__(self):
        self.cpus = []

    def add_cpu(self, obj):
        self.cpus.append(obj)

    def show_cpus(self):
        print("Computer contains:", [x.name for x in self.cpus])

obj = Computer()
obj.add_cpu(CPU("Example 1"))
obj.add_cpu(CPU("Example 2"))
obj.show_cpus()
