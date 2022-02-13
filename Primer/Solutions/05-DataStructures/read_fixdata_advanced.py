from handlers import *

__tokenseparator = "\x01"    # "\x01" is ASCII hex code 01, i.e. the "Start of Header" character in FIX.
__kvseparator = "="

__fix_jumptable = dict({
    "8"  : proc8,
    "9"  : proc9,
    "35" : proc35
}) 
	
# Split a line of FIX data into tokens, using __tokenseperator as the separator.		
def tokenize_line(line):
    tokens = line.split(__tokenseparator)
    table = dict(t.split(__kvseparator) for t in tokens)   # This is a "comprehension".
    return table

# Process a dictionary of key/value pairs.
def process_data(datadict):
    for k,v in datadict.items():	
        f = __fix_jumptable.get(k)
        if f:
            f(v)  
        else:
            proc_other(v)
			
# Main code.			
with open('fixdata.txt') as fh:
    for line in fh:
        datadict = tokenize_line(line)
        print(datadict)
        process_data(datadict)
