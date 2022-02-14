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

# Control Flow

- Conditional Statements
- Loops

---

# Conditional Statements

- Using if tests
- Nesting if tests
- Using the if-else operator
- Doing nothing
- Testing a value is in a set of values 
- Testing a value is in a range

---
layout: two-cols
---

# Using if tests 

<v-clicks>

Basic if tests

```python
if expression:
  body
```

if-else tests

```python 
if expression:
  body1
else:
  body2
```

</v-clicks>

::right::

<div v-click="5">

if-elif tests

```python
if expression1 :
  body1

elif expression2 :
  body2

elif expression3 :
  body3
…
else : 
  lastBody
```

</div>

<div v-click="6">

Notes:
- Test conditions can be any type of expression
- Use indentation to indicate the extent of a block, i.e. don't use {}

</div>


---
layout: two-cols
---
# Nesting if tests

You can nest if tests inside each other
- Use indentation to indicate level of nesting

::right:: 

Example:

```python
age = int(input("Please enter your age: "))
gender = input("Please enter your gender [M/F]: ").lower()

if age < 18:
  if gender == "m":
    print("Boy")
  else:
    print("Girl")
  
else: 
  if age >= 100: 
    print("Centurion")
   
  if gender == "m": 
    print("Man")
  else: 
    print("Woman")
  
print("The End")
```

---

# Using the if-else operator

The if-else operator is an in-situ test
- trueResult if condition else falseResult

Example:

```python
isMale = …
age    = …

togo = (65 - age) if isMale else (60 - age)

print("%d years to retirement" % togo)
```

---

# Doing nothing

<v-clicks>

If you're not sure what to do if a test is true…
- You can use the pass statement
- Equivalent to a null statement in other languages

Example:

```python
team = input("Who is your favourite rugby team? ")

if team == "Ireland":
  pass     # Eeek. We'll need to do something about this!

print("Your favourite team is %s " % team)
```

</v-clicks>

---

# Testing a value is in a set of values 

<v-clicks>

You can test if a value is in a set of allowable values
- Use the in operator

Example:

```python {all|1|3-4|6-7|9-10|12-13|all}
country = input("Please enter your country: ")

if country in ("Netherlands", "Belgium", "Luxembourg"):
  print("Lowlands country")

elif country in ("Norway", "Sweden", "Denmark", "Finland", "Iceland"):
  print("Nordic country")

elif country in ("England", "Scotland", "Wales", "Northern Ireland"):
  print("UK country")

else:
  print("%s isn't classified in this particular application!" % country) 
```

</v-clicks>

---

# Testing a value is in a range

<v-clicks>

You can test if a value is in a range of allowable values
- Call range(start,end) to return a range
- The range is inclusive at start, exclusive at the end 

Example:

```python {all|1|3-4|6-7|9-10|12-13}
number = int(input("Enter a football jersey number [1 to 11]: "))

if number == 1:
  print("Goalie")

elif number in range(2, 6):
  print("Defender")

elif number in range(6, 10):
  print("Midfielder")

else:
  print("Striker")
```

</v-clicks>

---

# Loops

- Using while loops
- Using for loops
- Using for loops with a range
- Unconditional jumps
- Using else in a loop
- Simulating do-while loops

---
layout: two-cols
---

# Using while loops

<v-clicks>

The while loop is the most straightforward loop construct

```python
while expression: 
  loopBody
```
- Test expression is evaluated
- If true, loop body is executed
- Test expression is re-evaluated
- Etc…

Note:
- Loop body will not be executed if test is false initially

</v-clicks>


::right::

<div v-click="6">

Example:

```python {all|2|3|4-5|3|4-5|all}
print("Numbers from 1-5 inclusive")
i = 1
while i <= 5:
  print(i)
  i = i + 1
```

</div>

---

# Using for loops

<v-clicks>

The for loop is different than in most languages
- In Python, a for loop iterates over items in a sequence

```python
for item in sequence:
  loopBody
```

Example:

```python {all|3|4|all}
lottonumbers = [2, 7, 3, 12, 19, 1]

for item in lottonumbers:
  print(item)
```

</v-clicks>

---

# Using for loops with a range

<v-clicks>

You can also use a for loop to iterate over a numeric range
- Use range() to create a range of numbers
- The for loop will iterate over these numbers

Example:

```python {all|1-3|5-7|9-11|all}
print("Numbers from 0-4 inclusive")
for i in range(5):
  print(i)
  
print("Numbers from 6-10 inclusive")
for i in range(6, 11):
  print(i)
  
print("First 5 odd numbers")
for i in range(0, 9, 2):
  print(i + 1)
```

</v-clicks>

---

# Unconditional jumps

<v-clicks>

Python provides two ways to perform an unconditional jump in a loop
- break
- continue

Example:

```python {all|3-8|5|6|10-15|12|13|all}
magicnumber = int(input("What is the magic number? "))

print("This loop terminates if it hits the magic number")
for i in range(1, 21):
  if i == magicnumber:
    break
  print(i)
print("End")

print("\nThis loop skips the magic number")
for i in range(1, 21):
  if i == magicnumber:
    continue
  print(i)
print("End")
```

</v-clicks>

---

# Using else in a loop

<v-clicks>

You can define an else clause at the end of a loop
- Same kind of syntax as if…else
- The else branch is executed if the loop terminates naturally (i.e. if it didn't exit because of a break)

Example
```python {all|5|6|8-9|all}
magicnumber = int(input("What is the magic number? "))

print("This loop does some processing if it doesn't detect the magic number")
for i in range(1, 21):
  if i == magicnumber:
    break
  print(i)
else:
  print("The magic number %d was not detected" % magicnumber)

print("End")
```

</v-clicks>

---

# Simulating do-while loops

<v-clicks>

Many languages have a do-while loop
- Guarantees at least one iteration through the loop body
- The test is at the end, to determine whether to repeat

Python doesn't have a do-while loop, but you can emulate it as follows

```python {all|1|3|4|all}
while True:
  exammark = int(input("Enter a valid exam mark: "))
  if exammark >= 0 and exammark <= 100:
    break
  
print("Your exam mark is %d" % exammark)
```

</v-clicks>

---

# Any questions?