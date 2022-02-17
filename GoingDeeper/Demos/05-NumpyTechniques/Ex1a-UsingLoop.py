import numpy as np
from timeit import default_timer as timer
import random


def compute_cubes_loop(data):
    result = np.empty(len(data))
    for i in range(len(data)):
        result[i] = data[i] ** 3
    return result


def create_random_list():
    returnList = []

    for item in range(10_000_000):
        returnList.append(random.randint(1, 10))
    return returnList


def compute_cubes(input):
    returnList = []

    for item in input:
        returnList.append(item ** 3)

    return returnList


# np.random.seed(0)
start1 = timer()
data = np.random.randint(1, 10000, size=10_000_000)

data1 = create_random_list()
end1 = timer()

print(f"It took {end1 - start1}  to generate the list.")

start = timer()
cubes = compute_cubes_loop(data)
end = timer()

startNative = timer()
cubes1 = compute_cubes(data1)
endNative = timer()

print('Execution time using a loop (np)', end - start)
print('Execution time using a loop (native)', endNative - startNative)
