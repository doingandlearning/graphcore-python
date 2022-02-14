class BankAccount:
    """Simple BankAccount class"""
    
    __nextId = 1
    __OVERDRAFT_LIMIT = -1000

    def __init__(self, accountHolder="Anonymous"):
        self.accountHolder = accountHolder
        self.__balance = 0.0
        self.id = BankAccount.__nextId
        BankAccount.__nextId += 1

    def deposit(self, amount):
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        newBalance = self.__balance - amount
        if newBalance < BankAccount.__OVERDRAFT_LIMIT:
            print("Insufficient funds to withdraw %f" % amount)
        else:
            self.__balance = newBalance
        return self.__balance

    def toString(self):
        return "{0} {1}, {2}".format(self.id, self.accountHolder, self.__balance)

    @classmethod		
    def getOverdraftLimit(cls):
        return cls.__OVERDRAFT_LIMIT

    @staticmethod		
    def getBanner():
        return "\nThis is the BankAccount Banner"


# client code (invoking methods via class name)
print(BankAccount.getBanner())
print(BankAccount.getOverdraftLimit())

acc1 = BankAccount("Luke")
print(acc1.getBanner())
print(acc1.getOverdraftLimit())

		
