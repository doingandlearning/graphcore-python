class BankAccount:
    """Simple BankAccount class"""
    
    __nextId = 1
    __OVERDRAFT_LIMIT = -1000

    def __init__(self, accountHolder="Anonymous"):
        self.accountHolder = accountHolder
        self.balance = 0.0
        self.id = BankAccount.__nextId
        BankAccount.__nextId += 1

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        newBalance = self.balance - amount
        if newBalance < BankAccount.__OVERDRAFT_LIMIT:
            print("Insufficient funds to withdraw %f" % amount)
        else:
            self.balance = newBalance
        return self.balance

    def __str__(self):
        return "{0} {1}, {2}".format(self.id, self.accountHolder, self.balance)

    def getOverdraftLimit():
        return BankAccount.__OVERDRAFT_LIMIT


class SavingsAccount(BankAccount):
    """Simple SavingsAccount class"""

    __DEFAULT_INTEREST_RATE = 1.5     
    
    def __init__(self, accountHolder="Anonymous", interestRate=None):
        super().__init__(accountHolder)
        if interestRate is None:
            self.interestRate = SavingsAccount.__DEFAULT_INTEREST_RATE
        else:
            self.interestRate = interestRate
            
    def earnInterest(self):
        self.balance *= (1 + self.interestRate)
        return self.balance 

    def withdraw(self, amount):
        if amount > self.balance:
            print("You can't go overdrawn in a savings account!")
        else:
            super().withdraw(amount)
        return self.balance

    def __str__(self):
        baseStr = super().__str__()
        return "{0}, {1}".format(baseStr, self.interestRate)

