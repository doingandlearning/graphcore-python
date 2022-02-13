---
# try also 'default' to start simple
theme: default
# random image from a curated Unsplash collection by Anthony
# like them? see https://unsplash.com/collections/94734566/slidev
# apply any windi css classes to the current slide
class: 'text-center'
# https://sli.dev/custom/highlighters.html
highlighter: shiki
# show line numbers in code blocks
lineNumbers: true
# some information about the slides, markdown enabled
info: |
  ## Slidev Starter Template
  Presentation slides for developers.

  Learn more at [Sli.dev](https://sli.dev)
# persist drawings in exports and build
drawings:
  persist: false
---

# Data Structures

---

- Sequence types
- Using sequences
- Set types
- Mapping types
- Additional techniques
- Worked examples

---

# 1. Sequence Types

- Overview
- Lists
- Splitting and joining
- Tuples
- Ranges

---

# Overview 

Basic sequence types
- List, tuple, and range

Text sequence types
- String

Binary sequence types
- bytes, bytesarray, and memoryview

---

# Lists

There are several ways to create a list
- []
- [item, item, item … ]
- list()
- list(iterable)

Example:

```python
list1 = []
list2 = ["Italy", "France", "Spain"]
list3 = [3, 12, 19, 1, 2, 7]
list4 = list()
list5 = list(list3)
list6 = list("Hello")

print("list1 has %d items: %s" % (len(list1), list1))
print("list2 has %d items: %s" % (len(list2), list2))
print("list3 has %d items: %s" % (len(list3), list3))
print("list4 has %d items: %s" % (len(list4), list4))
print("list5 has %d items: %s" % (len(list5), list5))
print("list6 has %d items: %s" % (len(list6), list6))
```

---

# Splitting and Joining

A common scenario where lists crop up in Python is when you call split() or join() on a string
- split() - splits a string into a list of substrings
- join()  - joins a list into a concatenated string

Example:

```python
str = "and we were singing, hymns and arias, land of my fathers, ar hyd yr nos"

words = str.split(", ")

lines = "...\n".join(words)

print("%s" % lines)
```

---

# Tuples

There are several ways to create a tuple
- ()
- a, or (a,)
- a,b,c or (a,b,c)
- tuple()
- tuple(iterable)

Example:
```python
tuple1 = ()
tuple2 = "Norway",     # or:  tuple2 = ("Norway",)
tuple3 = 3, 19, 2      # or:  tuple3 = (3, 19, 2)
tuple4 = tuple()
tuple5 = tuple(tuple3)

print("tuple1 has %d items: %s" %   (len(tuple1), tuple1))
print("tuple2 has %d item(s): %s" % (len(tuple2), tuple2))
print("tuple3 has %d items: %s" %   (len(tuple3), tuple3))
print("tuple4 has %d items: %s" %   (len(tuple4), tuple4))
print("tuple5 has %d items: %s" %   (len(tuple5), tuple5))
```

---

# Ranges

To create a range, use the range constructor
- range(stop)
- range(start, stop)
- range(start, stop, step)

Example:

```python
def display_range(msg, r):
    print("\n" + msg)
    for i in r:
        print(i)
        
range1 = range(5)
range2 = range(5,10)
range3 = range(5,10,2)

display_range("range1", range1)
display_range("range2", range2)
display_range("range3", range3)
```

---

# 2. Using Sequences

- Common sequence operations
- Slicing operations
- Unpacking operations
- Sequence modification operations
- Optional exercise

---

# Common sequence operations

You can perform these operations on any sequence:

```python
euro = ["GB", "ES", "NL", "F", "D", "I", "P"]
asia = ["SG", "JP"]

print("%s" % "P" in euro)               # True
print("%s" % "F" not in euro)           # False
print("%s" % (euro + asia))             # ['GB', 'ES', 'NL', 'F', 'D', 'I', 'P', 'SG', 'JP']
print("%s" % (asia * 2))                # ['SG', 'JP', 'SG', 'JP']
print("%s" % (2 * asia))                # ['SG', 'JP', 'SG', 'JP']
print("%d" % len(euro))                 # 7
print("%s" % min(euro))                 # D
print("%s" % max(euro))                 # P
print("%d" % euro.index("NL"))          # 2
print("%d" % euro.index("NL", 1))       # 2
print("%d" % euro.index("NL", 1, 4)     # 2
print("%d" % euro.count("ES"))          # 1
```

---

# Slicing operations


```python
euro = ["GB", "ES", "NL", "F", "D", "I", "P"]
asia = ["SG", "JP"]

print("%s" % (euro[1]))                 # ES
print("%s" % (euro[1:5]))               # ['ES', 'NL', 'F', 'D']
print("%s" % (euro[1:5:2]))             # ['ES', 'F']
print("%s" % (euro[3:]))                # ['F', 'D', 'I', 'P']
print("%s" % (euro[:-3]))               # ['GB', 'ES', 'NL', 'F'] 
```

---

# Unpacking operations

You can unpack (i.e. extract) elements in a sequence

The following example illustrates the techniques available

```python
euro = ["GB", "ES", "NL", "F"]

# Manually getting items.
a, b, c, d = euro[0], euro[1], euro[2], euro[3]
print("%s %s %s %s" % (a, b, c, d))    # GB ES NL F

# Unpacking.
e, f, g, h = euro
print("%s %s %s %s" % (e, f, g, h))    # GB ES NL F

# Catch-all unpacking.
i, j, *k = euro
print("%s %s %s" % (i, j, k))          # GB ES ['NL', 'F']
```

---

# Sequence modification operations

You can perform these operations on a mutable sequence such as a list:

```python
euro = ["GB", "ES", "NL", "F"]

euro[0] = "CY"
euro[1:3] = ["US", "AU", "AT"]
euro.append("SW")
euro.extend(["YU", "ZR"])
euro.insert(1, "NI")
print("%s" % euro)      # ['CY', 'NI', 'US', 'AU', 'AT', 'F', 'SW', 'YU', 'ZR']

euro.pop()
euro.pop(1)
del euro[2:4]
print("%s" % euro)      # ['CY', 'US', 'F', 'SW', 'YU']

euro.remove("US")
euro.reverse()
print("%s" % euro)      # ['YU', 'SW', 'F', 'CY']

eurocopy = euro.copy()
euro.clear()
print("%s" % eurocopy)  # ['YU', 'SW', 'F', 'CY']
print("%s" % euro)      # []
```

---

# Optional exercise

Write a Python program as follows:
- Ask the user to enter a series of numbers (-1 to quit)
- Determine which numbers are prime
- Display the prime numbers on the console

For detailed instructions:
See the Notes underneath this slide

For the solution code:
See Solutions\05-DataStructures\primes.py

---

# 3. Set Types

- Creating a set
- Creating a frozen set
- Common set operations
- Set modification operations

---

# Creating a set

There are several ways to create a set
- {item, item, item, … }
- set()
- set(iterable)
- Via a comprehension, similar to lists

Example:

```python
set1 = {"dog", "ant", "bat", "cat", "dog"}
set2 = set()
set3 = set(("dog", "ant", "bat", "cat", "dog"))
set4 = set("abracadabra")
set5 = {c.upper() for c in "abracadabra"}

print("set1 has %d items: %s" % (len(set1), set1))
print("set2 has %d items: %s" % (len(set2), set2))
print("set3 has %d items: %s" % (len(set3), set3))
print("set4 has %d items: %s" % (len(set4), set4))
print("set5 has %d items: %s" % (len(set5), set5))
```

---

# Creating a frozen set

Creating a frozenset is similar to creating a set
- Use the frozenset constructor

Example:

```python
set1 = frozenset({"dog", "ant", "bat", "cat", "dog"})
set2 = frozenset()
set3 = frozenset(("dog", "ant", "bat", "cat", "dog"))
set4 = frozenset("abracadabra")
set5 = frozenset({c.upper() for c in "abracadabra"})

print("set1 has %d items: %s" % (len(set1), set1))
print("set2 has %d items: %s" % (len(set2), set2))
print("set3 has %d items: %s" % (len(set3), set3))
print("set4 has %d items: %s" % (len(set4), set4))
print("set5 has %d items: %s" % (len(set5), set5))
```

---

# Common set operations

You can perform these operations on any set:

```python
s1 = {"GB", "US", "SG"}
s2 = {"GB", "US", "AU"}
s3 = {"F", "BE", "CA"}

print("%s" % ("GB" in s1))         # True
print("%s" % ("GB" not in s1))     # False

print("%s" % (s1.isdisjoint(s2)))  # False
print("%s" % (s1.isdisjoint(s3)))  # True

print("%s" % (s1.issubset(s2)))    # False
print("%s" % (s1 <= s2))           # False
print("%s" % (s1 < s2))            # False

print("%s" % (s1.issuperset(s2)))  # False
print("%s" % (s1 >= s2))           # False
print("%s" % (s1 > s2))            # False

print("%s" % (s1.union(s2, s3)))   # {'GB', 'US', 'BE', 'F', 'CA', 'AU', 'SG'}
print("%s" % (s1 | s2 | s3))       # {'GB', 'US', 'BE', 'F', 'CA', 'AU', 'SG'}

print("%s" % (s1.difference(s2, s3))) # {'SG'}
print("%s" % (s1 - s2 - s3))          # {'SG'}

print("%s" % (s1.symmetric_difference(s2))) # {'AU', 'SG'}
print("%s" % (s1 ^ s2))                     # {'AU', 'SG'}
```

---

# Set modification operations

You can perform these operations on a mutable set:

```python
s1.add("HK")
s1.remove("US")
s1.discard("D")
print("%s" % s1)       # {'SG', 'HK', 'GB'}

print("%s" % s1.pop()) # SG
print("%s" % s1)       # {'HK', 'GB'}

s1.update(s2,s3)
s1 |= s4 | s5
print("%s" % s1)       # {'D', 'AU', 'US', 'I', 'F', 'P', 'N', 'GB', 'CA', 'HK'}

s1.intersection_update(s2,s3)
s1 &= s4 & s5
print("%s" % s1)       # {'GB', 'US'}

s1.difference_update({"AA", "BB"},{"CC", "GB"})
s1 -= {"DD", "EE"} | {"FF", "GG"}
print("%s" % s1)       # {'US'}

s1.symmetric_difference_update(s2)
s1 ^= s2
print("%s" % s1)       # {'US'}
```

---

# 4. Mapping Types

- Creating a dictionary
- Iterating over a dictionary
- Accessing items in a dictionary 

---

# Creating a dictionary

There are several ways to create a dict
{key:value, key:value, … }
dict()
dict(anotherDict)
dict(keyword=value, keyword=value, … )
dict(zip(keysIterable, valuesIterable))

Example:

# Iterating over a dictionary
# Accessing items in a dictionary 