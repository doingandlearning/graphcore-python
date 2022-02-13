import sys

def proc8(num1, num2):
    print("Hi from proc8 with %d %d" % (num1, num2))

def proc35(num1, num2):
    print("Hi from proc35 with %d %d" % (num1, num2))


# Client
token = input("Enter a token: ")

try:
    funcName = "proc" + token
    funcPtr = getattr(sys.modules[__name__], funcName)
    funcPtr(42, 52)
except AttributeError as e:
    print("No handler function for token: %s" % token)