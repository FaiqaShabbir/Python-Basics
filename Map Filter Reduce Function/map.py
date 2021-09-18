# instead using lambda function we will use here user defined function

"""
def new(b):
    return b*b


x = map(new, (1, 2, 3, 4, 5))
print(list(x))
# print(tuple(x))
print(type(x))
"""


def new(a, b):
    return a*b


x = map(new, (1, 2, 3, 4, 5), (8, 9, 5, 4, 4, 2))
print(list(x))
# print(tuple(x))
print(type(x))
