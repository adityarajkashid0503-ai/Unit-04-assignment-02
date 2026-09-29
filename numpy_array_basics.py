import numpy as np

# Method 1: create array using list
arr1 = np.array([1,2,3,4,5,6,7,8,9,10])

# Method 2: create array using arange
arr2 = np.arange(1,11)

# Display both arrays and their properties
print("Array created using np.array():", arr1)
print("Array created using np.arange():", arr2)

print("\nBasic properties of the array:")
print("Data type:", arr1.dtype)
print("Shape:", arr1.shape)
print("Number of dimensions:", arr1.ndim)
print("Size (total elements):", arr1.size)

# Check both arrays are equal
print("\nAre both arrays equal?", np.array_equal(arr1, arr2))

# Vectorized operations
print("\nVectorized operations:")
print("arr1 * 2     :", arr1 * 2)
print("arr1 + 100   :", arr1 + 100)
print("sum(arr1)    :", arr1.sum())
print("mean(arr1)   :", arr1.mean())

# Indexing and slicing
print("\nIndexing and slicing:")
print("First element  :", arr1[0])
print("Last element   :", arr1[-1])
print("First 5 values :", arr1[:5])
print("Every other    :", arr1[::2])
