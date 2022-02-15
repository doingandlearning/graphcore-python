lines = []
test = "This is a test"
with open('dwarfs.txt', 'r') as fh:
    i = 1
    lines = []
    for line in fh:
        test = "Test string"
        lines.append(line)
        print("[%d] %s" % (i, line))
        i += 1

print(lines, i, test)