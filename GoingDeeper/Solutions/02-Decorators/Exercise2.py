#---Decorator to count calls to a function--------------------------------
def countCalls(func) :

    def innerFunc(*args, **kwargs) :
        innerFunc.calls += 1
        return func(*args, **kwargs)

    innerFunc.calls = 0
    
    return innerFunc


#---Decorator to cache calls and results----------------------------------
def cacheResults(func) :

    def innerFunc2(*args, **kwargs) :
        cacheKey = args + tuple(kwargs.items())
        if cacheKey not in innerFunc2.cache:
            innerFunc2.cache[cacheKey] = func(*args, **kwargs)
        return innerFunc2.cache[cacheKey] 

    innerFunc2.cache = dict()
    
    return innerFunc2


#---Decorated function----------------------------------------------------
@countCalls
@cacheResults
def fib(n) :
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)    
  
  
  
#---Client code----------------------------------------------------------
print("fib(20) is %d" % fib(20))
print("call count is %d" % fib.calls)

