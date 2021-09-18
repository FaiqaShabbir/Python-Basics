# filter within map

my_list = list(map(lambda x: x+x, filter(lambda x: x > 3, [3, 4, 6, 7])))
print(my_list)


# map within filter
new_list = tuple(filter(lambda x: x > 3, map(lambda x: x+x, [3, 4, 6, 7])))
print(new_list)
