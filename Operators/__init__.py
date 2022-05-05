from random import random

# 1st way to implement ternary operator
a, b = random(), random()
res = "a" if a > b else "b"
# print(res)

# Using Python Tuples to implement
# print((b, a)[a > b])
# print((f"b: {b}", f"a: {a}")[a > b])

# Using Python Dictionaries
var = {False: f"b: {b}",
       True: f"a: {a}"}[a > b]
print(var)

# Using Lambdas
var1 = (lambda: f"b : {b}", lambda: f"a: {a}")[a > b]()
print(var1)

rank = 1
print(id(rank))
identity = id
print(identity(3))
