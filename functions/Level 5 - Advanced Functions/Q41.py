# Question 41
# Create a function inside another function and demonstrate how the inner function works.

def outer():
    print("Outer function")

    def inner():
        print("Inner function")

    inner()

outer()
