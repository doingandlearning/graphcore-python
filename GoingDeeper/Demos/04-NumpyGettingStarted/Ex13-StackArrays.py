import numpy as np

# Create some arrays with same number of columns (2), and stack vertically.
a = np.array([10, 11])
b = np.array([[20, 21], [30, 31]])
result1 = np.vstack([a, b])
print(result1)         # [[10 11] [20 21] [30 31]]
print(result1.shape)   # (3, 2)      

# Create some arrays with same number of rows (2), and stack horizontally.
c = np.array([[40, 41], [50, 51]])
d = np.array([[60], [61]])
result2 = np.hstack([c, d])
print(result2)         # [[40 41 60] [50 51 61]]
print(result2.shape)   # (2, 3) 
