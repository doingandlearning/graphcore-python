import sys

try:
    fh = open('favNum.txt')
    str = fh.readline()
    num = int(str.strip())
    print("The number in the file is %d" % num)
	
except OSError as err:
    print("OSError occurred: %s" % err)

except ValueError as err:
    print("ValueError occurred: %s" % err)

except:
    print("Some other error occurred")

else:
    print("All completed OK!")
    fh.close()	
	
finally:
    print("That's all folks. This message will always appear!")
