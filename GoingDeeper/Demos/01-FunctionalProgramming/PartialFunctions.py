from functools import partial

multiply = lambda x,y: x * y

times2 = partial(multiply, 2)
times5 = partial(multiply, 5)
times8 = partial(multiply, 8)

print("10 times 2 is %d" % times2(10))
print("10 times 5 is %d" % times5(10))
