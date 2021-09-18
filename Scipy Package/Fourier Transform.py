from scipy.fftpack import fft, ifft
import numpy as np

x = np.array([1, 2, 3, 4])
y = fft(x)
print(y)
