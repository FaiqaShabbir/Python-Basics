def new(i):
    if i/2 >= 3:
        return i


my_list = list(filter(new, [6, 4, 8, 1, 12, 6, 78]))
print(my_list)
