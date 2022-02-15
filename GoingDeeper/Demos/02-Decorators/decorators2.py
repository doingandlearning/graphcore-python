#---Start of decorator---------------------------------------------------
def simpleDecorator(func) :

    # Define an inner function, wraps the decorated func.
    def innerFunc() :
        print("Start of simpleDecorator()")    
        func()
        print("End of simpleDecorator()")
   
    # Return the inner function.
    return innerFunc

#---End of decorator-----------------------------------------------------


# Some function, which we now decorate explicitly.
@simpleDecorator
def myfunc1() :
    print("Hi from myfunc1()")
  
  
  
#---Client code----------------------------------------------------------

print("###No need to manually wrap myfunc1 now, just invoke it directly...")
myfunc1()