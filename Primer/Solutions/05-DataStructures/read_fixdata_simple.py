from handlers import *

__tokenseparator = "\x01"    # "\x01" is ASCII hex code 01, i.e. the "Start of Header" character in FIX.
__kvseparator = "="

# Split a line of FIX data into tokens, using __tokenseperator as the separator.		
def tokenize_line(line):
    tokens = line.split(__tokenseparator)

    table = dict()
    for token in tokens:
        kv = token.split(__kvseparator)    
        key = kv[0]
        value = kv[1]
        table[key] = value   		# in table, insert an item with the specified key and value
    return table	

# Process a dictionary of key/value pairs.
def process_data(datadict):
    for k,v in datadict.items():	
        if k == "8":
            proc8(v)
        elif k == "9":
            proc9(v)
        elif k == "35":
            proc35(v)
        else:
            proc_other(v)
			
# Main code.			
with open('fixdata.txt') as fh:
    for line in fh:
        datadict = tokenize_line(line)
        print(datadict)
        process_data(datadict)
