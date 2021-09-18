from functools import reduce


def new(x, y):
    return x+y


my_list = reduce(new, [3, 4, 6, 7, 8, 9])
print(my_list)
