import numpy as np

a = np.array([[10], [11], [12]])
print(a.shape)  # (3,1)

b = np.array([20, 21, 22])
print(b.shape)  # (3,)
# (1, 3)

# [[20, 21, 22]]
# [[20, 21, 22], [20, 21, 22], [20, 21, 22]] (3,3)

# [[10, 10, 10], [11, 11, 11], [12, 12, 12]] (3,3)

result = a + b
print(result.shape)  # (3, 3)
print(result)  # [[30 31 32] [31 32 33] [32 33 34]]