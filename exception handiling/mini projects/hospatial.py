class InvalidPatientError(Exception):
    pass


class DoctorNotAvailableError(Exception):
    pass


class InvalidAppointmentError(Exception):
    pass


class Hospital:
    def __init__(self):
        self.doctors = ["Dr. Kumar", "Dr. Priya"]

    def book_appointment(self, name, age, doctor, date):

        if name == "" or age <= 0:
            raise InvalidPatientError("Invalid patient details")

        if doctor not in self.doctors:
            raise DoctorNotAvailableError("Doctor not available")

        if date == "":
            raise InvalidAppointmentError("Invalid appointment date")

        print("Appointment booked successfully")


hospital = Hospital()

try:
    hospital.book_appointment(
        "Lilly",
        18,
        "Dr. Priya",
        "20-08-2026"
    )

except InvalidPatientError as e:
    print(e)

except DoctorNotAvailableError as e:
    print(e)

except InvalidAppointmentError as e:
    print(e)