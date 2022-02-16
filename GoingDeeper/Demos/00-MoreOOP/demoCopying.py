from accounting import BankAccount

from copy import copy


print("\nInitially...")
acc1a = BankAccount("Fred")
print(acc1a.toString())  # 100

print("\nDemo two refs to same object...")
acc1b = acc1a
acc1b.deposit(100)
print(acc1a.toString())  # 100
print(acc1b.toString())  # 100

print("\nDemo copying an object...")
acc2 = copy(acc1a)
acc2.deposit(200)
print(acc1a.toString())  # 100
print(acc1b.toString())  # 100
print(acc2.toString())   # 300
