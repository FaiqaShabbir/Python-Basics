# less memory

import numpy as np
import time
import sys

"""
s = range(1000)
print(sys.getsizeof(5)*len(s))

d = np.arange(1000)
print(d.size*d.itemsize)
"""

size = 1000000
L1 = range(size)
L2 = range(size)

A1 = np.arange(size)
A2 = np.arange(size)

start = time.time()
result = [(x, y) for x, y in zip(L1, L2)]
print((time.time()-start)*1000)

start = time.time()
result = A1 + A2
print((time.time()-start)*1000)
