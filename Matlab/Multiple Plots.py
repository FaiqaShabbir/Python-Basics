import matplotlib.pyplot as plt
import numpy as np


def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)


t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

# 211 = 2:vertically 2 plots, 1:horizontally 1 plot 1: 1 graph 1 vertical graph
# means last one shows position that it it will at first
plt.subplot(122)
plt.plot(t1, f(t1), 'bo', t2, f(t2))

# Then it will be on second number
plt.subplot(121)
plt.plot(t2, np.cos(2*np.pi*t2))
plt.show()

"""
211 and 212 shows that graphs will be places vertically but
but only one horizontally
"""