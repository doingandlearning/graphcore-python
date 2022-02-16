#---Define your decorator functions here---------------------------------
from time import time

def countCalls(func):
    def innerFunc(*args, **kwargs):
        innerFunc.calls += 1
        return func(*args, **kwargs)

    innerFunc.calls = 0
    return innerFunc


def cacheResults(func):
    def innerFunc2(*args, **kwargs):
        cacheKey = args + tuple(kwargs.items())
        if cacheKey not in innerFunc2.cache:
            innerFunc2.cache[cacheKey] = func(*args, **kwargs)
        return innerFunc2.cache[cacheKey]

    innerFunc2.cache = dict()

    return innerFunc2

def timeit(func):
    def innerFunc(*args, **kwargs):
        ts = time()
        returnVal = func(*args, **kwargs)
        te = time()
        print(f"This function took {(te-ts)}")
        return returnVal
    return innerFunc


#---Function to be decorated---------------------------------------------


@countCalls
@cacheResults
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)    


#---Client code----------------------------------------------------------

@timeit
def fib20():
    return fib(2000)

fib20()

print("fib(20) is %d" % fib(20))
print("call count is %d" % fib.calls)


