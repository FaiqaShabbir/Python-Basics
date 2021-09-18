"""
reduce():
            Applies some other function to b list of elements that are
            passed as parameter to it and finally returns b single value
"""

from functools import reduce

# syntax(function,sequence) ; function  = lambda
print(reduce(lambda a, b: a + b, [23, 21, 45, 98]))
