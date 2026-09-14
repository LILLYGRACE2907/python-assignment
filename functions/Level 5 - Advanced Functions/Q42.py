# Question 42
# Create a function that returns another function.

def outer():
    def inner():
        return "Hello from returned function"
    return inner

message = outer()
print(message())
