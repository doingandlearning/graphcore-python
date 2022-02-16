# Import functools, a standard Python module containing various decorators.
from functools import wraps, lru_cache


# ---Decorator to count calls to a function--------------------------------
def countCalls(func):
    # The @wraps decorator preserves metadata about the wrapped function.
    @wraps(func)
    def innerFunc(*args, **kwargs):
        innerFunc.calls += 1
        return func(*args, **kwargs)

    innerFunc.calls = 0

    return innerFunc


# ---Decorated function----------------------------------------------------
# The @lru_cache decorator caches the last 30 calls to fib().
@countCalls
@lru_cache(30)
def fib(n):
    """My cool Fibonacci function"""
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

    # ---Client code----------------------------------------------------------


print("fib(20) is %d" % fib(20))
print("call count is %d" % fib.calls)

print("The name of the function is %s" % fib.__name__)
print("The doc for the function is %s" % fib.__doc__)
