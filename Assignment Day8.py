# Create a Numpy array
#
# with random values
#
import numpy as np
arr1d = np.random.rand(3)
arr2d = np.random.rand(2,3)
arr3d = np.random.rand(2,3,2)
print(arr1d)
print(arr2d)
print(arr3d)

# (4x2) empty and a full NumPy array
arr = np.empty((4,2))
print(arr)
#
# (3x5) array filled with all zeros
arr = np.zeros((3,5))
print(arr)
#
# (4x3x2) array filled with all ones
arr = np.ones((4,3,2))
print(arr)
#
# Write a NumPy program to create a 3x3 2D matrix with values ranging from 2 to 10.
arr = np.array([[2,3,4],[5,6,7],[8,9,10]])
print(arr)
#
# Write a NumPy program to create a null vector of size 10 and update the sixth value to 11.
arr = np.zeros(10)
print(arr)
arr[5] = 11
print(arr)

#
# Write a NumPy program to reverse an array (the first element becomes the last).
arr = np.array([2,3,4,5,6,7,8,9,10])
print(arr)
arr = arr[::-1]
print(arr)
#
# Write a NumPy program to convert an array to a floating type.
arr = np.array([2,3,4,5,6,7,8,9,10])
print(arr.dtype)
arr = arr.astype(float)
print(arr.dtype)
print(arr)

