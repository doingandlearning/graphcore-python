import numpy as np
from scipy import stats

data = np.random.rand(100_000_000)

print('Sum            ', np.sum(data))
print('Product        ', np.prod(data))
print('Minimum        ', np.min(data))
print('Maximum        ', np.max(data))
print('Mean           ', np.mean(data))
print('Median         ', np.median(data))
print('Mode           ', stats.mode(data))
print('Variance       ', np.var(data))
print('Std dev        ', np.std(data))
print('50th percentile', np.percentile(data, 50))

