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
print("""
=========================
= FORMATTED INFORMATION =
=========================
  Name: %s
  You'll be %d soon!
=========================""" % (name, age))

# Do some string concatenation.
city = input("What city do you live in? ")
country = input("What country? ")
address = "You " "live " "in " + city + ", " + country + "."
print(address)
