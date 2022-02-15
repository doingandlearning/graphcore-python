#---Decorator to count calls to a function--------------------------------
def countCalls(func) :

    def innerFunc(*args, **kwargs) :
        innerFunc.calls += 1
        return func(*args, **kwargs)

    innerFunc.calls = 0
    
    return innerFunc


#---Decorated function----------------------------------------------------
@countCalls
def fib(n) :
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)    
  
  
  
#---Client code----------------------------------------------------------
print("fib(20) is %d" % fib(20))
print("call count is %d" % fib.calls)

