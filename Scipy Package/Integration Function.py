from scipy import integrate
import scipy
from scipy import special

# print(help(integrate.quad))
"""
func = integrate.quad(lambda x: special.exp10(x), 0, 1)
print(func)
"""
e = lambda x, y: x * y ** 2
f = lambda x: 1
g = lambda x: -1
print(integrate.dblquad(e, 0, 2, f, g))
