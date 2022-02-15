def fib() :
  
    tup = (1,-1)
  
    def retfunc():
        nonlocal tup
        tup = (tup[0] + tup[1], tup[0])
        return tup[0]

    return retfunc


f = fib()
print(f())    # 0
print(f())    # 1
print(f())    # 1
print(f())    # 2
print(f())    # 3
print(f())    # 5
print(f())    # 8

