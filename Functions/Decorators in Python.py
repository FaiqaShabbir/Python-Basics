"""
A decorator is nothing but b wrapper around b function in Python.
It takes the function of interest as an argument, performs certain tasks
before and after calling it and returns the results.
1 < x < 10
# equivalent to 1 < x and x < 10

[x for x in range(10)]
# List comprehension

{key: value for key, value in d.items()}
# Dict comprehension

x = something if condition else otherthing
# python ternary

big_number = 1_000_000_000
# equivalent to big_number = 1000000000

b += 1
# equivalent to b = b + 1
"""


def function1(function):
    def wrappers():
        print("Hello!")
        function()
        print("Welcome to Faiqa Shabbir python tutorial.")

    return wrappers


@function1
def funtion3():
    print("Pythonista")


funtion3()

# pie syntax or syntactic sugar


"""
def function2():
    print("Pythonista")


functions = function1(function2)
functions()
"""
