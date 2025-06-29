# Combining a one and a two-dimensional NumPy Array
import numpy as np
arr1d = np.array([1,2,3,4])
arr2d = np.array([[1,2,3,4],[2,3,4,5]])
arr2d = np.reshape(arr2d, (-1))
arr3 = np.concatenate((arr1d, arr2d))
print(arr3)
#
# Flatten a 2d numpy array into 1d array
arr2d = np.array([[1,2,3,4],[2,3,4,5]])
arr1d = np.reshape(arr2d, (-1))

# Reverse a numpy array

arr = np.array([1, 2, 3, 4, 5])
reversed = arr[::-1]

print(reversed)

# Practice operations like
# - Get the maximum value from given array
res = np.argmax(arr)
print(arr[res])

# - Get the minimum value from given array
res = np.argmin(arr)
print(arr[res])
# - Find the number of rows and columns of a given array using NumPy
arr = np.array([[1,2,3],[234,2,3]])
print("Rows and col : ",arr.shape)
# - Select the elements from a given array (each element and specific element)
a = np.array([1,2,3,4,5])
print("Each element: ", a[::])
ind = int(input("Enter the index for specific element"))
print("Element: ", a[ind])

# - Find the sum of values in a 2D array using for loop
sum = 0
for rows in arr2d:
    for i in rows:
        sum += i
print(sum)
# - Adding, Subtracting, multiplying, dividing arrays in Numpy
a = np.array([[1,2],[7,8]])
b = np.array([[1,2],[11,12]])
print(a+b)
print(a-b)
print(a*b)
print(a/b)
