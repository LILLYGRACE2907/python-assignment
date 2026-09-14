class InvalidPatientError(Exception):
    pass


class Hospital:
    def add_patient(self, name, age):
        try:
            if name == "":
                raise InvalidPatientError("Patient name cannot be empty")

            if age <= 0:
                raise InvalidPatientError("Invalid patient age")

            print("Patient added")
            print("Name:", name)
            print("Age:", age)

        except InvalidPatientError as e:
            print(e)


hospital = Hospital()

hospital.add_patient("Lilly", 18)
hospital.add_patient("", 20)
hospital.add_patient("Ravi", -5)