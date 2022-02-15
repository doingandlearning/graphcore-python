import numpy as np

# Create a 1-D array, index into it, and modify elements.
a = np.array([0, 10, 20, 30, 40, 50, 60, 70])
print(a)
print(a[1])        # 10
print(a[-1])       # 70
a[1] = 111
print(a)

# Create a 2-D array, index into it, and modify elements.
b = np.array([[0, 10, 20, 40], [50, 60, 70, 80]])
print(b)
print(b[0, 1])     # 10
print(b[0, -1])    # 40
print(b[-1, 1])    # 60
print(b[-1, -1])   # 80
b[0, 1] = 111
print(b)
