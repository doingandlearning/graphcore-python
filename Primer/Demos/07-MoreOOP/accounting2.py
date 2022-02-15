class BankAccount:
    """Simple BankAccount class"""
    
    __nextId = 1
    __OVERDRAFT_LIMIT = -1000

    def __init__(self, accountHolder="Anonymous"):
        """Initializes a BankAccount with a given name, generated id, and 0 balance"""
        self.accountHolder = accountHolder
        self.__balance = 0.0
        self.id = BankAccount.__nextId
        BankAccount.__nextId += 1

    def deposit(self, amount):
        """Deposits money into an account, and returns new balance"""
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        """Withdraws money from an account (if sufficent funds), and returns new balance"""
        newBalance = self.__balance - amount
        if newBalance < BankAccount.__OVERDRAFT_LIMIT:
            print("Insufficient funds to withdraw %f" % amount)
        else:
            self.__balance = newBalance
        return self.__balance

    def toString(self):
        """Returns a string representation of a BankAccount"""
        return "{0} {1}, {2}".format(self.id, self.accountHolder, self.__balance)

    def getOverdraftLimit():
        """Returns overdraft limit for all accounts"""
        return BankAccount.__OVERDRAFT_LIMIT

help(BankAccount())