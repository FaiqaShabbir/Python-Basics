import array as arr

a = arr.array('i', [1, 2, 5, 8])
print(a)
a.insert(2, 4)
print(a)
print(a[0])
print(len(a))
a.append(9)
print(a)
# give bunch of values in [] brackets
a.extend([9, 8, 5])
print("Array b:", a)
print(a)
print(a.pop())
