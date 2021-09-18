"""
Note: “We use the “wildcard” or “*” notation like this –
*args OR **kwargs – as our function’s argument when we have
doubts about the number of  arguments we should pass in b
function.”
# Python program to illustrate
# *args with first extra argument
def myFun(arg1, *argv):
    print ("First argument :", arg1)
    for arg in argv:
        print("Next argument through *argv :", arg)

myFun('Hello', 'Welcome', 'to', 'GeeksGeeks')

"""


def function1(function):
    def wrapper(*args, **kwargs):
        print("Hello!")
        function(*args, **kwargs)
        print("Welcome to Faiqa Shabbir Python  tutorial")
    return wrapper


@function1
def functions(name):
    print(f"{name}")


functions("Faiqa Shabbir")
