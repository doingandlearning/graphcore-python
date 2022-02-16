# Import the standard JSON module.
import json

# A Python list.
coords = [ { "x": 100, "y": 150, "z": [
    1, 2, 3, {"name": "Kevin"}
] }, { "x": 200, "y": 250 } ]

# Dump Python list into a JSON string. 
coordsJson = json.dumps(coords, indent=4)  

# Use the JSON string (e.g. in a real example, send it to a REST service).
print(coordsJson)

with open("output.json", "w") as fh:
    fh.write(coordsJson)

