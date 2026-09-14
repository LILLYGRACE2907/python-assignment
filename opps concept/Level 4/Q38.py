# Question 38
# A Teacher is a Person. Identify the relationship and implement it.

# Relationship: IS-A

class Person:
    def show(self):
        print("This is Person")

class Teacher(Person):
    def action(self):
        print("This is Teacher")

obj = Teacher()
obj.show()
obj.action()
