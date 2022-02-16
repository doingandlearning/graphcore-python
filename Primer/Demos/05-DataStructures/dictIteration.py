dialcodes = {"us": "+1", "nl": "+31", "no": "+47"}

print("Items:")
for keys,values in dialcodes.items():
    print(keys, values)

print("\nKeys:")
for k in dialcodes.keys():
    print(k)
    
print("\nValues:")
for v in dialcodes.values():
    print(v)

