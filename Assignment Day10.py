# Replace Nan with 0 and Interchange 3 rows and 3 columns of 2D array
# [[6, -8, 73, -110], [np.nan, -8, 0, 94]]
import numpy as np
ar = np.array([[6, -8, 73, -110], [np.nan, -8, 0, 94],[9 , 56, 89, 5]])
print(ar)
ar = np.nan_to_num(ar, copy=True, nan=0.0)
print(ar)
ar[[0,1,2],:] = ar[[1,2,0],:]
print("After changing rows: ", ar)
ar[:,[0,1,2]] = ar[:,[1,2,0]]
print("After changing columns: ", ar)
#
# Move axes of 3D array to new positions
ar = np.arange(1,13)
ar = np.reshape(ar, (2,2,3))
print(ar)
ar[[0,1],:,:] = ar[[1,0],:,:]
print("After changing sets: ", ar)
#
# Replace NaN values with average of columns
import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, None, 4],
    'B': [None, 2, 3, 4],
    'C': [1, None, None, 4]
})


df.fillna(df.mean(numeric_only=True), inplace=True)

print(df)

#
# Replace negative value with zero in NumPy array using replace
import numpy as np

arr = np.array([3, -5, 7, -2, 0, 4])
arr = np.where(arr < 0, 0, arr)

print("Array after replacing negatives with 0:", arr)
#
# Study the following program
# Import NumPy as np
#
# python
# Copy
# Edit
# # create a NumPy 1d-arrays
# arr1 = np.array([3, 4])
# arr2 = np.array([1, 0])
# Find average of NumPy arrays
#
# python
# Copy
# Edit
# avg = (arr1 + arr2) / 2
# print("Average of NumPy arrays:\n", avg)
# Calculate average, mean, median, mode values of two NumPy 2D-arrays
a1 = np.array([[1, 2], [3, 4]])
a2 = np.array([[5, 6], [7, 8]])
combined = np.concatenate((a1.flatten(), a2.flatten()))

print("Average:", np.mean(combined))
print("Mean:", np.mean(combined))
print("Median:", np.median(combined))

#
# Solve the following equation using linalg() and inverse Matrix method:
#
# diff
# Copy
# Edit
# x - 2y + 3z = 9
# -x + 3y - z = -6
# 2x - 5y + 5z = 17
A = np.array([
    [1, -2, 3],
    [-1, 3, -1],
    [2, -5, 5]
])
B = np.array([9, -6, 17])

solution = np.linalg.inv(A).dot(B)
print("Solution [x, y, z]:", solution)
# Using "Customizing Matplotlib Visualizations" discussed in NumPy session 4 notes, plot graph to compare your at least 2 semester result
#
import matplotlib.pyplot as plt

subjects = ['sub1', 'sub2', 'sub3', 'sub4', 'sub5']
sem3 = [56,57,59,60,54]
sem2 = [49,55,64,59,58]
plt.plot(subjects, sem3, color='red' , linestyle = '--')
plt.plot(subjects, sem2, color='blue' , linestyle = '--')
xlabel = "Subjects"
ylabel = "Marks"
plt.title("Comparison of last 2 sem marks")
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.show()

