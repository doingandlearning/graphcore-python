

#---Start of decorator---------------------------------------------------
def simpleDecorator(func):

    # Define an inner function, wraps the decorated func.
    def innerFunc(*args, **kwargs):
        print("Start of simpleDecorator()")    
        returnValue = func(*args, **kwargs)
        print("End of simpleDecorator()")
        return returnValue
   
    # Return the inner function.
    return innerFunc

#---End of decorator-----------------------------------------------------


# Some function, which we now decorate explicitly.
@simpleDecorator
def myfunc1(first_name, last_name, nationality):
    print(f"{first_name} {last_name} is {nationality}")
    return True

def myfunc2():
    pass
  

  
#---Client code----------------------------------------------------------

print("###No need to manually wrap myfunc1 now, just invoke it directly...")
result = myfunc1("Kevin", "Cunningham", "Northern Irish")

print(result)