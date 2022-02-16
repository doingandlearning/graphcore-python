---
# try also 'default' to start simple
theme: default
# random image from a curated Unsplash collection by Anthony
# like them? see https://unsplash.com/collections/94734566/slidev
# apply any windi css classes to the current slide
class: 'text-center'
# https://sli.dev/custom/highlighters.html
highlighter: shiki
# show line numbers in code blocks
lineNumbers: true
# some information about the slides, markdown enabled
info: |
  ## Slidev Starter Template
  Presentation slides for developers.

  Learn more at [Sli.dev](https://sli.dev)
# persist drawings in exports and build
drawings:
  persist: false
---

# Decorators

---

1. Getting started with decorators
2. Additional decorator techniques
3. Parameterized decorators

---

# 1. Getting started with decorators

- Overview
- Defining a decorator function
- Applying a decorator function manually
- Applying a decorator function properly

---

# Overview

<v-clicks>

Python allows you to decorate functions and classes using the @decorator syntax

The decorator enhances the function/class with extra capabilities

```python
@someDecorator
def someFunction(…) :
   …
```

```python
@someDecorator
class SomeClass :
   …
```

This section shows how to define decorators
- We'll see how to define decorator functions
- We'll also describe how Python applies decorator functions

</v-clicks>

---
layout: two-cols
---

# Defining a decorator function (1/2)

<v-clicks>

Define a function that takes a function pointer as an argument
- The pointer indicates the target function you want to decorate

Inside the decorator function, implement a nested function 
- The nested function should call the target function
- And should also perform the desired decoration behaviour

At the end of the decorator function, return a pointer to the nested function 

</v-clicks>

::right::

<div v-click="4">

```python {all|1|4-7|10|all}
def simpleDecorator(func) :

    # Define an inner function, which wraps (decorates) the target function.
    def innerFunc() :
        print("Start of simpleDecorator()")    
        func()
        print("End of simpleDecorator()")
   
    # Return the inner function.
    return innerFunc
```

</div>

---
layout: two-cols
---

# Applying a decorator function manually

<v-clicks>

In order to understand how decorators work, let's first of all see how to apply a decorator function manually:


Line 6 calls the decorator function manually, passing a pointer to the target function as an argument
- This statement returns a pointer to the inner function

Line 7 calls the inner function
- This invokes the target function, with the desired decoration

</v-clicks>

::right::


```python {all|6|7|all}
# Some function that we want to decorate.
def myfunc1() :
    print("Hi from myfunc1()")

# Client code.
pointerToInnerFunc = simpleDecorator(myfunc1)    
pointerToInnerFunc()                             
```

---

# Applying a decorator function properly

<v-clicks>

The previous slide showed how to call a decorator function manually, to wrap a target function

Now let's see how to apply a decorator function properly, i.e. using the @decorator syntax

```python
# Some function, which we now decorate explicitly.
@simpleDecorator
def myfunc1() :
    print("Hi from myfunc1()")

# Client code.
myfunc1()
```

Note the client code just calls myfunc1() directly
- Python intervenes, thanks to the @simpleDecorator decorator, and converts the code to the equivalent of the previous slide

</v-clicks>

---

# Additional decorator techniques

- Decorating a function that takes arguments
- Decorating a function that returns a result

---

# Decorating a function that takes arguments

<v-clicks>

Consider the following function, which takes arguments
Note that we've decorated the function

```python
@parameterAwareDecorator
def myfunc1(firstName, lastName, nationality) :
    print(f"Hi {firstName} {lastName}, your nationality is {nationality}")
```

This is how to define the decorator function
- The inner function receives variadic args and passes to target func

```python
def parameterAwareDecorator(func) :

   def innerFunc(*args, **kwargs) :
        print("Start of parameterAwareDecorator()")    
        func(*args, **kwargs)
        print("End of parameterAwareDecorator()")
   
   return innerFunc
```

Client code:

```python
myfunc1("Ola", "Nordmann", "Norsk")
myfunc1(nationality="Cymraeg", lastName="Cunningham", firstName="Jayne")
```

</v-clicks>

---

# Decorating a function that returns a result

<v-clicks>

Consider the following function, which returns a result

```python
@returnAwareDecorator
def myfunc1(firstName, lastName, nationality) :
    return f"Hi {firstName} {lastName}, your nationality is {nationality}"
```

This is how to define the decorator function
- The inner function returns the result of the target function

```python {all|5|7|all}
def returnAwareDecorator(func) :

    def innerFunc(*args, **kwargs) :
        print("Start of returnAwareDecorator()")    
        returnValueFromFunc = func(*args, **kwargs)
        print("End of returnAwareDecorator()")
        return returnValueFromFunc
        
    return innerFunc
```

Client code:

```python
res1 = myfunc1("Kari", "Nordmann", "Norsk")
res2 = myfunc1(nationality="Cymraeg", lastName="Cunningham", firstName="Kevin")
```

</v-clicks>

---

# Parameterized decorators

- Overview
- Defining a parameterized decorator
- Applying a parameterized decorator manually
- Applying a parameterized decorator properly

---

# Overview

<v-clicks>

Decorators can take parameters, to make them flexible

E.g. imagine a flexible decorator that displays custom pre/post messages around a target function call
- You might apply the decorator as follows
- The decorator takes parameters specifying the pre/post messages

```python
@parameterizedDecorator("HELLO", "GOODBYE")
def myfunc1(firstName, lastName, nationality) :
    return "Hi %s %s, your nationality is %s" % (firstName, lastName, nationality)
```

</v-clicks>

---
layout: two-cols
---
# Defining a Parameterized Decorator

Here's how to define a parameterized decorator

```python {all|1|3-16|4|7-11|13|16|all}
def parameterizedDecorator(prefix, suffix) :

    # Define inner function, which just wraps a function.
    def innerFunc1(func) :
    
        # Define inner-inner function, which decorates/calls target function.
        def innerFunc2(*args, **kwargs) :
            print(prefix)    
            returnValueFromFunc = func(*args, **kwargs)
            print(suffix)
            return returnValueFromFunc
            
        # Return innerFunc2, i.e. the inner-inner function.    
        return innerFunc2
        
    # Return innerFunc1, i.e. the inner function.
    return innerFunc1
```

::right::

We have a layering of functions, to handle all the args:
- Arguments to the decorator itself
- The target function to be invoked
- Arguments to pass in to the target function

---
layout: two-cols
---
# Applying a Parameterized Decorator Manually 


In order to understand how parameterized decorators work, let's first see how to apply the decorator manually:

```python {all|6|7|8|all}
# Some function, which we don't decorate explicitly here.
def myfunc1(firstName, lastName, nationality) :
    return "Hi %s %s, your nationality is %s" % (firstName, lastName, nationality) 
  
# Client code
pointerToInnerFunc1 = parameterizedDecorator("HELLO", "GOODBYE")  
pointerToInnerFunc2 = pointerToInnerFunc1(myfunc1)                
res = pointerToInnerFunc2("Per", "Nordmann", "Norsk")            
```



::right::

<v-clicks>

Line 6 calls the decorator manually, passing args into it
- This statement returns a pointer to innerFunc1

Line 7 calls innerFunc1, passing target function into it
- This just return a pointer to innerFunc2

Line 8 calls innerFunc2, passing args for the target func
- This invokes the target func, with the desired decoration

</v-clicks>

---

# Applying a Parameterized Decorator Properly

<v-clicks>

The previous slide showed how to call a parameterized decorator function manually, to wrap a target function

Now let's see how to apply a parameterized decorator function properly, i.e. using the @decorator syntax


```python
# Some function, which we now decorate explicitly.
@parameterizedDecorator("HELLO", "GOODBYE")
def myfunc1(firstName, lastName, nationality) :
    return "Hi %s %s, your nationality is %s" % (firstName, lastName, nationality)

# Client code.
res1 = myfunc1("Kari", "Nordmann", "Norsk")
```

Note the client code just calls myfunc1() directly
- Python intervenes, thanks to the @parameterizedDecorator, and cascades through the necessary sequence of function calls and argument-passing


</v-clicks>

---

# Any questions?