class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("In __init__() for %s and %d" % (self.name, self.age))

    def __del__(self):
        print("In __del__() for %s and %d" % (self.name, self.age))
    
    def __repr__(self):
        return "{0} instance, name: {1}, age: {2}".format( \
                                                      self.__class__.__name__,\
                                                      self.name, self.age)
    def __str__(self):
        return "{0} is {1}.".format(self.name, self.age)

    def __eq__(self, other):
        return self.age == other.age

    def __ne__(self, other):
        return self.age != other.age

    def __lt__(self, other):
        return self.age < other.age

    def __gt__(self, other):
        return self.age > other.age

    def __le__(self, other):
        return self.age <= other.age

    def __ge__(self, other):
        return self.age >= other.age


# Client code.
p1 = Person("Bill", 23)
p2 = Person("Ben", 25)

print(repr(p1))
print(str(p2))

print("p1 == p2 gives %s" % (p1 == p2))
print("p1 != p2 gives %s" % (p1 != p2))
print("p1 <  p2 gives %s" % (p1 <  p2))
print("p1 >  p2 gives %s" % (p1 >  p2))
print("p1 <= p2 gives %s" % (p1 <= p2))
print("p1 >= p2 gives %s" % (p1 >= p2))

del p1, p2
