# Stream of number can be generated at any range may

# it is even or other

"""
num = range(100)
loop = (x for x in num)
print(loop)

for y in loop:
    pass
print(y)
"""

# for even
num = range(2, 100, 2)
loop = (x for x in num)
print(loop)

for y in loop:
    print(y)
