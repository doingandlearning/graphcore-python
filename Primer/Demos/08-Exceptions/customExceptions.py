# Custom exception class.
class MyError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
		

# Client code.
try:
    raise MyError("EEK ERROR ERROR ERROR")
	
except MyError as err:
    print("It appears my exception occurred, the value is %s" % err.value)		