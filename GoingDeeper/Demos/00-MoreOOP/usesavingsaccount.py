from accounting import SavingsAccount

acc1 = SavingsAccount("Fred", 3.0)
acc1.deposit(100)
acc1.earnInterest()
acc1.withdraw(500)

print(acc1)
