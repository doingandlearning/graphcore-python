# Get the user's name and age, from stdin.
name = input("Enter your name: ")
ageStr = input("Enter your age: ")

# Convert the age from a string to an int.
age = int(ageStr)

# Calculate the user's age next birthday.
age += 1

# Output a simple message.
print("%s, you will be %d next birthday" % (name, age))

# Output a formatted message.
print(f"""
=========================
= FORMATTED INFORMATION =
=========================
  Name: {["hello", "david"]}
  You'll be {5.53} soon!
=========================""")

# Do some string concatenation.
city = input("What city do you live in? ")
country = input("What country? ")
address = "You " "live " "in " + city + ", " + country + "."
print(address)
