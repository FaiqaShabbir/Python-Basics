import numpy as np

arr = np.array([(1, 2, 3), (4, 7, 9)])
arr1 = np.array([(10, 11, 12), (13, 14, 15)])
"""print("Axis of array:", arr.sum(axis=1))
print("Square Root:\n", np.sqrt(arr))
print("Standard Deviation:\n", np.std(arr))"""

print("Vertical Stacking:\n", np.hstack(arr))
print(arr1.ravel())
