from scipy import linalg
import numpy as np

arr = np.array([[1, 2], [3, 4]])
inverse = linalg.inv(arr)
print(inverse)