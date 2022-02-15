class BankAccount:
    """Simple BankAccount class"""
    
    __nextId = 1
    __OVERDRAFT_LIMIT = -1000

    def fromString(str):
        str = str.rstrip("\r\n")
        fields = str.split(",")
        acc = BankAccount()
        acc.id = int(fields[0])
        acc.accountHolder = fields[1]
        acc.__balance = float(fields[2])
        return acc
        
    def __init__(self, accountHolder="Anonymous"):
        self.accountHolder = accountHolder
        self.__balance = 0.0  # _BankAccount__balance
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
        return "{0},{1},{2}".format(self.id, self.accountHolder, self.__balance)

    def getOverdraftLimit():
        return BankAccount.__OVERDRAFT_LIMIT

