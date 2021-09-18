"""
filter():

         Used to filter given iterable(list,sets,etc) with help
         of another function which should be passed as an argument
         yo test all elements to be true or false.
"""

my_list = [6, 7, 9, 0, 3, 4, 5, 1]
# syntax: filter(function, iterable)
new_list = list(filter(lambda a: (a/3 == 2 or a/2 == 2), my_list))
print(new_list)
