import array as arr

a = arr.array('d', [9.4, 7.3, 3.1, 8.9, 1.0, 2.6, 1.1, 2.2, 3.7])
print("In For Loop:")
for x in a[0:6]:
    print(x)
print("In while Loop:")
b = 0
while b < len(a[0:-3]):
    print(a[b])
    b = b+1
