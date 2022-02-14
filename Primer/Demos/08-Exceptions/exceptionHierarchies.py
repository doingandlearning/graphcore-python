import sys

try:
    fh = open('favNum.txt')
    str = fh.readline()
    num = int(str.strip())
    print("The number in the file is %d" % num)
	
except FileNotFoundError as err:
    print("File not found: %s" % err)

except OSError as err:
    print("More general OSError occurred: %s" % err)

except ValueError as err:
    print("ValueError occurred: %s" % err)

except:
    print("Some other error occurred")

else:
    print("All completed OK!")
    fh.close()	