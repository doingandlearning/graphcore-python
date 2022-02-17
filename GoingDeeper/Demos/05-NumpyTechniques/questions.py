import numpy as np

testArray = np.array([[2, 3, 4, 5], [1, 2, 3, 4], [5, 6, 7, 1]])

# Masking an array but keep the same shape
mask_result = np.where(testArray > 2, testArray, 0)
print("masked array\n", mask_result)

# Deleting a row from an array
delete_result = np.delete(testArray, 1, 1)  # Note: Doesn't change the original data!
print("deleted array\n", delete_result)

# Sorting rows based on one columns value.
sorted_array = testArray[np.argsort(testArray[:, 1])]
print("sorted array\n", sorted_array)
