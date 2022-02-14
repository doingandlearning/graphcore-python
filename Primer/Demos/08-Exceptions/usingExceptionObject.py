# Keep on looping until the user enters a number.
while True:
    	
    try:
        inp = input("What's your favourite number? ")
        num = int(inp)
        print("Thanks, your favourite number is %d" % num)
        break
		
    except ValueError as err:
        print("ValueError occurred: %s" % err)