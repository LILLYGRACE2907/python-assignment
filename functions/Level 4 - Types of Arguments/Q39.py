# Question 39
# Create a function using **kwargs to create and display a person's profile.

def profile(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

profile(name="Lilly", age=20, city="Pithapuram", course="CCN")
