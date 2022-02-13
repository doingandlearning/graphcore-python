honorific = input("Honorific, e.g. Mr. or Mrs.: ")
firstname = input("First name: ")
lastname  = input("Last name: ")

formattedName = "{0} {1}. {2}".format(honorific.title(),
                                      firstname[0].upper(),
                                      lastname.title())
print("Your name is %s" % formattedName)

email   = input("Email address: ")
pincode = input("4-digit pin code (fictional): ")

is_valid = "@" in email and len(pincode) == 4 and pincode.isdigit()
if is_valid:
    print("Email address %s, pin code %s" % (email.lower(), pincode))
else:
    print("Your details are valid")
