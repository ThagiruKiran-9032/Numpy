import numpy as np


# Task 1: Array Indexing
print("Task 1: Array Indexing")
numbers = np.array([10, 20, 30, 40, 50])
matrix = np.array([[1, 2, 3], [4, 5, 6]])

print("1D array:", numbers)
print("First element:", numbers[0])
print("Third element:", numbers[2])
print("Element in row 2, column 3:", matrix[1, 2])


# Task 2: Negative Indexing
print("\nTask 2: Negative Indexing")
print("Last element:", numbers[-1])
print("Second-to-last element:", numbers[-2])
print("Last element in the second row:", matrix[-1, -1])


# Task 3: Array Slicing
print("\nTask 3: Array Slicing")
print("Elements from index 1 to 3:", numbers[1:4])
print("Every other element:", numbers[::2])
print("First two columns of the 2D array:\n", matrix[:, :2])


# Task 4: Array Iteration
print("\nTask 4: Array Iteration")
print("Iterating through the 1D array:")
for value in numbers:
    print(value)


# Task 5: 2D Array Iteration
print("\nTask 5: 2D Array Iteration")
print("Iterating through rows:")
for row in matrix:
    print(row)

print("Iterating through every element:")
for row in matrix:
    for value in row:
        print(value)


# Task 6: Array Reshaping
print("\nTask 6: Array Reshaping")
values = np.arange(1, 13)
reshaped = values.reshape(3, 4)
print("Original 1D array:", values)
print("Reshaped to 3 rows and 4 columns:\n", reshaped)


# Task 7: Flatten and Ravel
print("\nTask 7: Flatten and Ravel")
original = np.array([[1, 2, 3], [4, 5, 6]])
flattened = original.flatten()
flattened[0] = 100
print("After changing flatten() result:", flattened)
print("Original array is unchanged:\n", original)

raveled = original.ravel()
raveled[0] = 200
print("After changing ravel() result:", raveled)
print("Original array changes with ravel():\n", original)


# Task 8: Concatenation and Stacking
print("\nTask 8: Concatenation and Stacking")
first_array = np.array([[1, 2], [3, 4]])
second_array = np.array([[5, 6], [7, 8]])

joined_rows = np.concatenate((first_array, second_array), axis=0)
joined_columns = np.concatenate((first_array, second_array), axis=1)
print("Concatenation with axis=0 (add rows):\n", joined_rows)
print("Concatenation with axis=1 (add columns):\n", joined_columns)
print("Vertical stacking:\n", np.vstack((first_array, second_array)))
print("Horizontal stacking:\n", np.hstack((first_array, second_array)))


# Task 9: Array Splitting
print("\nTask 9: Array Splitting")
split_array = np.arange(1, 9)
equal_parts = np.split(split_array, 4)
print("Original array:", split_array)
print("Split into 4 equal sections:", equal_parts)

unequal_array = np.arange(1, 8)
print("Trying to split an array of 7 elements into 3 equal sections:")
try:
    np.split(unequal_array, 3)
except ValueError as error:
    print("Could not split into equal sections:", error)

print("The program continues after the splitting error.")
