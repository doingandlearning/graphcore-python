from datetime import datetime

class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
        self.__startdate = datetime.now()

    def payRaise(self, amount):
        self.__salary += amount

    def __repr__(self):
        return f"{self.__name} started on {self.__startdate}"

emp1 = Employee("Kevin", 1000)
emp2 = Employee("Kevin", 1000000)

emp2.payRaise(1000000)

print(emp1)
print(emp2)