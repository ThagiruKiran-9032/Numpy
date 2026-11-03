import numpy as np  


# Task 1: Import NumPy
print("Task 1: NumPy is imported.")


# Task 2: Create 1D, 2D, zeros, and ones arrays
print("\nTask 2: Creating basic arrays")
one_dimensional = np.array([1, 2, 3, 4])
two_dimensional = np.array([[1, 2, 3], [4, 5, 6]])
zeros_array = np.zeros((2, 3))
ones_array = np.ones((2, 3))

print("1D array:")
print(one_dimensional)
print("2D array:")
print(two_dimensional)
print("Zeros array:")
print(zeros_array)
print("Ones array:")
print(ones_array)


# Task 3: Generate number sequences with np.arange()
print("\nTask 3: Number sequences with np.arange()")
sequence = np.arange(0, 10, 2)
print(sequence)


# Task 4: Display common array attributes
print("\nTask 4: Array attributes")
print("Array:\n", two_dimensional)
print("ndim:", two_dimensional.ndim)
print("shape:", two_dimensional.shape)
print("size:", two_dimensional.size)
print("dtype:", two_dimensional.dtype)


# Task 5: Create arrays with 0, 1, 2, and 3 dimensions
print("\nTask 5: Array dimensions and shapes")
zero_dimensional = np.array(7)
one_dimensional_example = np.array([1, 2, 3])
two_dimensional_example = np.array([[1, 2], [3, 4]])
three_dimensional = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for label, array in (
    ("0D array", zero_dimensional),
    ("1D array", one_dimensional_example),
    ("2D array", two_dimensional_example),
    ("3D array", three_dimensional),
):
    print(f"{label}: ndim={array.ndim}, shape={array.shape}")
    print(array)


# Task 6: Create integer, float, and Boolean arrays and display their types
print("\nTask 6: Array data types")
integer_array = np.array([1, 2, 3])
float_array = np.array([1.5, 2.5, 3.5])
boolean_array = np.array([True, False, True])

for label, array in (
    ("Integer array", integer_array),
    ("Float array", float_array),
    ("Boolean array", boolean_array),
):
    print(f"{label}: {array}, dtype={array.dtype}")


# Task 7: Convert arrays between float and integer with astype()
print("\nTask 7: Converting array data types")
as_float = integer_array.astype(float)
as_integer = float_array.astype(int)
print("Integer array converted to float:", as_float, "dtype:", as_float.dtype)
print("Float array converted to integer:", as_integer, "dtype:", as_integer.dtype)


# Task 8: Marks mini challenge using array arithmetic, sum, and mean
print("\nTask 8: Marks mini challenge")
marks = np.array([85, 90, 78, 92, 88])
bonus_marks = marks + 5
total_marks = np.sum(bonus_marks)
average_marks = np.mean(bonus_marks)

print("Original marks:", marks)
print("Marks after adding 5 bonus points:", bonus_marks)
print("Total marks after bonus:", total_marks)
print("Average marks after bonus:", average_marks)
