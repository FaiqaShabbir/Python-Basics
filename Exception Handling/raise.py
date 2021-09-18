"""
x = 10
if x > 5:
    raise Exception("x should not exceed 5. The value of x was: {}".format(x))

import sys
assert ("linux" in sys.platform), "This code runs only on linux"
"""
import sys


def linux_interaction():
    assert ("linux" in sys.platform), "Function will run only on linux"
    print("Doing Something")


try:
    print(linux_interaction())
except:
    print("Alright!")

