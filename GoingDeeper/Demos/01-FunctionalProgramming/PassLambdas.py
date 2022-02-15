def apply(arg1, arg2, op) :
    return op(arg1, arg2)

result1 = apply(10, 20, lambda x, y: x + y)
print(result1)

result2 = apply(10, 20, lambda x, y: x / y)
print(result2)

