from accounting import BankAccount

acc1 = BankAccount("Fred")

# Set/add an attribute on an object.
setattr(acc1, "bonus", 2000)

# Test if an object has an attribute.
if hasattr(acc1, "bonus"):
    print("acc1.bonus is %d" % acc1.bonus)

# Remove an attribute from an object.
delattr(acc1, "bonus")
