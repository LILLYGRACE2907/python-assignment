class Teacher:
    def __init__(self, name, subject, experience):
        self.name = name
        self.subject = subject
        self.experience = experience

    def display(self):
        print("Name:", self.name)
        print("Subject:", self.subject)
        print("Experience:", self.experience, "years")
        print()


t1 = Teacher("Ravi", "Python", 5)
t2 = Teacher("Anita", "Java", 7)
t3 = Teacher("Suresh", "DBMS", 4)

t1.display()
t2.display()
t3.display()