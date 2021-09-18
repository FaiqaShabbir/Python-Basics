import array as arr

a = arr.array('b', [0, 1, 2, 3, 4])
b = arr.array('b', [5, 6, 7, 8])
c = arr.array('b', [9, 10])
# Leave the array empty in which you want to concatenate
d = arr.array('b')
d = a+b+c
print("Array concatenated as:", d)
