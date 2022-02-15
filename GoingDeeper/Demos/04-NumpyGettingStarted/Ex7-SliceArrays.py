import numpy as np

# Create a 1-D array, and get various slices.
a = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80,90])
print(a[3:])         # [30 40 50 60 70 80]
print(a[:3])         # [ 0 10 20]
print(a[3:7])        # [30 40 50 60]
print(a[3:7:2])      # [30 50]
print('FFGHGHFGHFGHF', a[3::2])       # [30 50 70]
print(a[::2])        # [ 0 20 40 60 80]

# Create a 2-D array, and get various slices in each dimension.
b = np.array([[0, 10, 20], [30, 40, 50], [60, 70, 80]])
print(b[1:, 1:])     # [ [40 50] [70 80] ]
print(b[:2, :2])     # [ [ 0 10] [30 40] ]
print(b[::2, ::2])   # [ [ 0 20] [60 80] ]

# Etc :-)