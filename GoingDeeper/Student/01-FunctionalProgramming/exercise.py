is_even = lambda x: x % 2 == 0

print(is_even(4))
print(is_even(5))

def negate(f):
    return lambda x: not f(x)

is_odd = negate(is_even)

print(is_odd(3))
print(is_odd(4))

myList = [100,101,102,103,104,105,106]

def nth(pos, iList):
    if pos == 0:
        return iList[0]
    else:
        return nth(pos-1, iList[1:])

print(nth(4, myList))
