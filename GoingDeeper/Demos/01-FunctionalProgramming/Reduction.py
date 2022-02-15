from functools import reduce

mylambda = lambda x,y: x+y

result = reduce(mylambda, [3,12,19,1,2,7])
print(result)
