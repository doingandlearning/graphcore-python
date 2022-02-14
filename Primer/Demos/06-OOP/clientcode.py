from accounting import BankAccount

# Create and use objects.
acc1 = BankAccount("Fred")
acc2 = BankAccount("Wilma")

# Invoke methods on objects.
acc1.deposit(200)
acc1.withdraw(50)
print("acc1 account holder is %s" % acc1.accountHolder)
#acc1.__balance += 1000000
print(acc1.toString())

# Access class-level members.
#print("Next ID is %d"         % BankAccount.__nextID)
#print("Overdraft limit is %d" % BankAccount.__OVERDRAFT_LIMIT)
print("Overdraft limit is %d" % BankAccount.getOverdraftLimit())

# Manage object references.
acc2a = BankAccount("Bill") 
acc2b = acc2a
acc2a.deposit(100)
print("acc2a is %s" % acc2a.toString())
print("acc2b is %s" % acc2a.toString())
del acc2b
del acc2a

