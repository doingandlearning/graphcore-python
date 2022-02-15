import numpy as np

# Create 1D array initially, for simplicity.
a = np.arange(5)
print(a)               # [0 1 2 3 4]
print(a[0])            # (5,)

# Create 2D array with 1 row, 5 columns. 
b = a[np.newaxis, :]   
print(b.shape)         # (1, 5)
print(b)
print(b[0, 0])

c = b[np.newaxis, :, :]
print(c.shape) 
print(c[0, 0, 0])