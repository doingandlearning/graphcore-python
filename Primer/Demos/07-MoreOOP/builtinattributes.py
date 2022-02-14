from accounting import BankAccount

print("BankAccount.__doc__:",    BankAccount.__doc__)
print("BankAccount.__name__:",   BankAccount.__name__)
print("BankAccount.__module__:", BankAccount.__module__)
print("BankAccount.__bases__:",  BankAccount.__bases__)
print("BankAccount.__dict__:",   BankAccount.__dict__)

acc1 = BankAccount("Ola")
print("acc1.__dict__:", acc1.__dict__)
