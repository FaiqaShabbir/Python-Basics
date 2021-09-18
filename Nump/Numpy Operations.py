import numpy as np

arr = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print("It is", arr.ndim, "dimension array")
print("Size of each element in array:", arr.itemsize)
print("Data type of each element in array:", arr.dtype)
print("Size of array:", arr.size)
print("Shape of array:", arr.shape)
"""
print("Before Reshaping:")
print(arr)
print("After Reshaping:")
print(arr.reshape(3, 2))
"""
print("Slicing:")
# [0:, 2] means that it will include element at index
# 2 from every array
print(arr[0:, 2])

# Here it will just add the element at index 2 from
# just 1st and 2nd array excluding 3rd one
print(arr[0:2, 1])
print("Line Space:")
# line space will print 6 values between 1 and 4
ar = np.linspace(1, 4, 6)
print(ar)
