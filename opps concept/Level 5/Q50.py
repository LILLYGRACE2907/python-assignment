# Question 50
# Create a University that HAS-A departments, IS-A type of educational institution, and USES-A examination service.

class EducationalInstitution:
    def show_type(self):
        print("Educational institution")

class Department:
    def __init__(self, name):
        self.name = name

class ExaminationService:
    def conduct_exam(self):
        print("Examination conducted")

class University(EducationalInstitution):
    def __init__(self):
        self.departments = [Department("CSE"), Department("ECE")]

    def conduct(self):
        print("University departments:", [d.name for d in self.departments])
        ExaminationService().conduct_exam()

u = University()
u.show_type()
u.conduct()
