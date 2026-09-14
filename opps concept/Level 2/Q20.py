# Question 20
# Create a Hospital class that HAS-A multiple Doctor and Patient objects.

class Doctor:
    def __init__(self, name):
        self.name = name

class Patient:
    def __init__(self, name):
        self.name = name

class Hospital:
    def __init__(self, doctors, patients):
        self.doctors = doctors
        self.patients = patients

    def show_details(self):
        print("Doctors:", [d.name for d in self.doctors])
        print("Patients:", [p.name for p in self.patients])

hospital = Hospital([Doctor("Dr. Ravi"), Doctor("Dr. Priya")],
                    [Patient("Asha"), Patient("Kiran")])
hospital.show_details()
