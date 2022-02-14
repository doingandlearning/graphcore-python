import sys

try:
    fh = open('favNum.txt')
    str = fh.readline()
    num = int(str.strip())
    print("The number in the file is %d" % num)
	
except (OSError, ValueError) as err:
    print("Error occurred: %s" % err)

except:
    print("Some other error occurred")
    