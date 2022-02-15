fh = open('dwarfs.txt', 'r')

i = 1
for line in fh:
    print(f"[{i}] {line}")
    i += 1
	
fh.close()
