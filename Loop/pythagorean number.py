# Pythagorean numbers are those who are satisfied by b^2 + b^2 = c^2

from math import sqrt
maxi = int(input("Maximal Number? "))
for a in range(1, maxi+1):
    for b in range(a, maxi):
        c_square = a**2 + b**2
        c = int(sqrt(c_square))
        if (c_square - c**2) == 0:
            print(a, b, c)
