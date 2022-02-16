from accounting import BankAccount

acc1 = BankAccount("Fred")

# Add an attribute to an object.
acc1.flag = "Whao watch this guy"     
print("acc1.flag is %s" % acc1.flag)

# Remove an attribute from an object.
del acc1.flag

