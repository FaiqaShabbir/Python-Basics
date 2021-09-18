import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 3*np.pi, 0.1)

y = np.sin(x)

z = np.cos(x)

plt.plot(x, y)
plt.show()

plt.plot(x, z)
plt.show()

v = np.tan(z)
plt.plot(v)
plt.show()
