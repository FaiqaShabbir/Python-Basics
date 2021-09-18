# in python everything is treated as object even functions
# Function is also known as b first-class object and functions can be passed around as arguments
# Inner function = function inside function
def user(name):
    return f"Hello {name}"


def greet(name):
    return f"{name} , how you doing?"


def learner(function4):
    return function4("Dear learner")


print(learner(user))
print(learner(greet))
