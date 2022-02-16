import re

names = ["Xander Harris", "Jennifer Smith", "Timothy Jones", "Amy Alexandrescu", "Peter Price", "Weifung Xu"]


# Method 1: The one liner
winners = [name for name in names if re.search("[Xx]", name)]
print(winners)
winners.clear()

# Method 2: The for loop

for name in names:
       result = re.search("[Xx]", name)
       if result:
              winners.append(name)

print(winners)
winners.clear()

# Method 3: The for loop with pre-compile

reObj = re.compile("[Xx]")

for name in names:
       result = reObj.search(name)
       if result:
              winners.append(name)

print(winners)

