def tailRecursiveFactorial(accumulator, n):
    if n == 0:
        return accumulator
    else: 
        return tailRecursiveFactorial(n * accumulator, n - 1)

result = tailRecursiveFactorial(1, 4)
print("4 factorial is %d\n" % result)
		