import matplotlib.pyplot as plt
from scipy import interpolate
from matplotlib import pyplot as plt
import numpy as np
x = np.arange(5, 20)
y = np.exp(x/3.0)
f = interpolate.interp1d(x, y)
x1 = np.arange(6, 12)
y1 = f(x1)
plt.plot(x, y, '^', x1, y1, '--')
plt.show()
