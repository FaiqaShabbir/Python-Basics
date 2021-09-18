"""
map():
        Applies b given function to all iterable and returns
        b new list!
"""

my_list = [6, 8, 9, 5, 4, 3, 2, 1, 7]
new_list = list(map(lambda a: (a/3 != 2), my_list))
print(new_list)
