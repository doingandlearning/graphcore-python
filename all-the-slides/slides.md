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

# Python Training

Kevin Cunningham

Grab repo at https://github.com/doingandlearning/graphcore-python

---

# A bit about me

- Lived, taught and developed in Brighton for 20 years
- Recently relocated back to Northern Ireland
- Dad to two boys
- Love learning new things
- You can find me on Twitter (@dolearning) or on my website (https://kevincunningham.co.uk)

---

# A bit about the course

> Let's look at Mindnode

---

# Timings

|               |           |
| ------------- | --------- |
| 9.30 - 10.45     | Session 1 |
| 10.45 - 11    | Coffee    |
| 12.00 - 1 | Lunch |
| 1.00 - 2.30   | Session 3 |
| 2.30 - 2.45   | Coffee    |
| 2.45 - 4.30   | Session 4 |

---

# A bit about you

- Your name and role
- Your programming and Python experience
- What you're hoping to get out of this course

---


# Getting Started With Python

---

- Setting the scene
- Running Python script code

- Creating virtual environment

> Demo folder: 01-GettingStarted

---

# 1. Setting the Scene

- Hello Python
- What can you do with Python?
- Downloading Python
- Using the Python documentation
- Installing Python packages

---

# Hello Python

<v-clicks>

- Python is a powerful and expressive programming language
  - Object-oriented
  - Dynamic typing
  - Interpreted

- Available on a wide range of platforms
  - Unix/Linux
  - Windows
  - Mac OS X
  - etc ...

</v-clicks>

---

# What can you do with Python?

<v-clicks>

- Scripting
- File I/O
- String handling and regular expressions
- Web applications and REST web services
- Data science

</v-clicks>

--- 

# Downloading Python

Are we all there?

- [Anaconda](https://www.anaconda.com/products/individual)
- [PyCharm CE](https://www.jetbrains.com/pycharm/download/#section=mac)

---

# Using Python Documentation

- [Docs available online at https://docs.python.org](https://docs.python.org)

---

# Installing Python Packages

<v-clicks>

There are many Python packages available
  - e.g. NumPy, MatPlotLib, etc.
  - [See https://pypi.python.org/pypi for details](https://pypi.python.org/pypi)

You can use the pip package manager to install Python packages:
- For example, to install the NumPy package:
```bash
pip install numpy
```

To find where pip installed a package:
```bash
pip show numpy
```

Note: These are already installed in Anaconda

</v-clicks>

---

# 2. Running Python Script

- Running Python script interactively
- Creating variables
- Line continuation
- Blocks
- Creating and running Python modules
- Python keywords

---

# Running Python Script Interactively

<v-clicks>

Run the Python interpreter in interactive mode, and execute Python code.

```bash
python
```

Then enter some Python code. For example:
```python
print("Hello World")
```

</v-clicks>

---

# Creating Variables

<v-clicks>

In Python, you don't need to declare a variable
  - Just assign it a value, and Python will create it for you dynamically

Rules for identifiers in Python
  - Can contain uppercase or lowercase letters, digits, and underscore 
  - But can't start with a digit

```python {all|1|2|3|4|all}
firstname = "Homer"
lastname = "Simpson"
fullname = firstname + " " + lastname
print(fullname)
```

</v-clicks>

---

# Line Continuation

<v-clicks>

If a statement spans multiple lines…
  - You can use `\` to continue from one line to the next

```python {all|1|2|3-5|6|all}
firstname = "Homer"
lastname = "Simpson"
fullname = firstname + \
" " + \
lastname
print(fullname)
```

</v-clicks>

---

# Blocks

<v-clicks>

Python uses indentation to denote blocks
- Don't use {} 
- Use `:` to indicate the start of an indented block

```python {all|1|2-3|4|all}
age = 21
if age >= 18 and age <= 30:
    print("You are eligible for an 18-30s holiday!")
print("That's all folks")
```

</v-clicks>

---

# Creating and Running Python Modules

<v-clicks>

You can put Python code into modules
- A module is just a script file containing Python code
- Typically starts with a lowercase letter and ends in `.py`

> greeting.py
```python
print("Hello Python!")
print("This is my module")
```

You can run the module via the Python interpreter

```bash
python greeting.py
```

</v-clicks>

---
layout:two-cols
---

# Python Keywords

Here is a full list of all the keywords in Python
- False, None, True
- if, elif, else, assert, is
- and, or, not
- for, in, from, while, break, continue, pass
- def, return, global, nonlocal, lambda
- import, from
- class, del 
- raise, try, except, as, finally
- with, as
- yield
- await, async

::right::

You can ask Python to tell you about all its keywords:

```python
import keyword
keyword.kwlist
```

---

# Any questions?

---

# Annex: Creating a Virtual Environment

- Overview
- Installing virtualenv
- Creating a virtual environment for a project
- Activating a virtual environment
- Using virtualenv
- Deactivating a virtual environment

---
layout: image-right
image: ./assets/python_environment_2x.png
---

# Overview

<v-clicks>

In your life as a Python developer, you'll likely create many applications that use diverse Python packages

Ideally you would like the applications to be independent of each other
- The Python packages you download for one application shouldn't interfere with the Python packages for other applications

To help you keep Python application environments isolated from each other, you can use the virtualenv tool

</v-clicks>

---

# Installing virtualenv

<v-clicks>

You install virtualenv via pip as a one-off exercise as follows:

```bash
pip install virtualenv
```

You can test you installation as follows:

```bash
virtualenv --version
```

</v-clicks>

---

# Creating a virtual environment for a project

<v-clicks>

To create a virtual environment for a particular project:

```bash
virtualenv MyProject
```

This command creates a folder named MyProject that contains:
- Python executable files
- A copy of the pip library, which you can use to install other packages (locally for this virtual environment)

</v-clicks>

---

# Activating a virtual environment

<v-clicks>

To begin using a virtual environment, you must activate it 

In Mac/Unix

```bash
source MyProject/bin/activate
```

In Windows:

```
MyProject\Scripts\activate
```

After you've activated a virtual environment, its name will appear in the command prompt.

</v-clicks>

---

# Using virtualenv

<v-clicks>

You can now use pip to installl packages into your virtual environment.
- e.g. to install the 'request' packages:
```bash
pip install requests
```
This will install the package into Lib/site-packages folder.

You can write a Python script that uses the package

```python
import requests
response = requests.get('https://httpbin.org/ip')
print('Your IP is {0}'.format(response.json()['origin']))
```

And run it as normal

```bash
python main.py
```

</v-clicks>

---

# Deactivating a virtual environment

<v-clicks>

You can deactivate a virtual environment as follows:

```bash
deactivate
```

This tears down your virtual environment
- You don't see the packages in that virtual environment any more
- You can reactivate it whenever you need to (see 2 slides previous)

</v-clicks>

---


# Python Language Fundamentals

---

- Defining and using modules
- Defining and using packages
- Basic data types

---

# Defining and using modules

- The Python standard library
- Understanding modules
- More about modules
- Listing the names in a module

---

# The Python standard library

<v-clicks>

Python defines an extensive and powerful standard library
- Comprises a large number of modules

Built-in modules are implemented in C
- Provide access to low-level system functionality
- E.g. file I/O

Other modules are implemented in Python

- See the Lib folder in the Python installation folder

For full info, see:
https://docs.python.org/3.10/library 

</v-clicks>

---

# Understanding modules

<v-clicks>

You can create your own Python modules
- Here's a simple module, which just defines some variables

> greetings.py
```python
morning = "Good morning"
afternoon = "Good afternoon"
evening = "Good evening"
```

To use a module elsewhere, use the import keyword
- Several ways to do this:

```python
import greetings
print(greetings.morning)
```

```python
from greetings import morning, afternoon
print(morning + " " + afternoon)
```
```python
from greetings import *
print(morning + " " + afternoon + " " + evening)
```

</v-clicks>

---

# More about modules

<v-clicks>

You can access the name of a module
Use the __name__ property

>usegreetings

```python
import greetings

print("Name of current module is %s" % __name__)
print("Name of greetings module is %s" % greetings.__name__)
```

Python only imports a given module once
- Regardless of how many times you try to import it

Python searches the following locations for a module
- The directory containing the input script (or the current directory)
- The directory specified by PYTHONPATH 
- The installation-dependent default

</v-clicks>

---

# Listing the names in a module

<v-clicks>

You can list all the names defined in a module
- Use the dir() built-in function

>listmodulenames.py
```python
import math
from greetings import morning, afternoon

print("Names in the math module:")
print(dir(math))

print("\nNames in the current module:")
print(dir())
```

</v-clicks>

---

# Defining and using packages

- Overview of packages
- Example modules
- Importing specific modules
- Aliasing imported modules
- Importing all modules

---

# Overview of packages

<v-clicks>

Python allows you to organise related modules into packages and sub-packages
- A package is a folder that contains a file named `__init__.py`

Example

```bash
utils/                    Top-level package, named utils.
    __init__.py           Initialize the utils package.
    constants/            Sub-package for constants.
        __init__.py       Initialize the constants package.
        metric.py
        physics.py
              ...
    messages/             Sub-package for messages.
        __init__.py       Initialize the messages package.
        french.py
        norwegian.py
              ...
```

</v-clicks>

---

# Example modules

<v-clicks>

Here are the modules we've defined in the utils package
Modules in the utils.constants sub-package:

```python
INCH_TO_CM = 2.54
MILE_TO_KM = 1.61
```

```python
ELECTRONIC_CHARGE = 1.602e−19
PLANCKS_CONSTANT = 6.626e−34
```

Modules in utils.messages sub-package:

```python
HELLO = "Bonjour"
GOODBYE = "Au revoir"
```

```python
HELLO = "Hei"
GOODBYE = "Ha det bra"
```

</v-clicks>

---

# Importing specific modules

<v-clicks>

To import specific module(s) from a package:

```python
import utils.constants.metric   

print("Inch to centimetre: %.4f" % utils.constants.metric.INCH_TO_CM)
print("Mile to kilometre:  %.4f" % utils.constants.metric.MILE_TO_KM)
```

To import specific module(s) from a package, into the current symbol namespace:

```python
from utils.constants import metric

print("Inch to centimetre: %.4f" % metric.INCH_TO_CM)
print("Mile to kilometre:  %.4f" % metric.MILE_TO_KM)
```

To import specific name(s) from a module from a package, into the current symbol namespace:

```python
from utils.constants.metric import INCH_TO_CM, MILE_TO_KM

print("Inch to centimetre: %.4f" % INCH_TO_CM)
print("Mile to kilometre:  %.4f" % MILE_TO_KM)
```

</v-clicks>

---

# Aliasing imported modules

<v-clicks>

You can specify a local alias for a module
- Use import … as

```python
# import a module and give it an alias.
import utils.constants.metric as metric

print("Alias example")
print("Inch to centimetre: %.4f" % metric.INCH_TO_CM)
print("Mile to kilometre:  %.4f" % metric.MILE_TO_KM)
```

</v-clicks>

---

# Importing all modules

<v-clicks>

You can use * to indicate you want to import all modules from a package

```python
from utils.messages import *

print("Hello in French:   %s"    % utils.messages.french.HELLO)
print("Goodbye in French: %s"    % utils.messages.french.GOODBYE)
print("Hello in Norwegian:   %s" % utils.messages.norwegian.HELLO)
print("Goodbye in Norwegian: %s" % utils.messages.norwegian.GOODBYE)
```

You must tell Python which modules to actually import from that package
- In the package's __init__.py file …
- Define a global variable named __all__ and set it to a list of all the modules to be imported

```python
__all__ = ["french", "norwegian"]
```

</v-clicks>

---

# Basic data types

- Numbers
- Numeric operators
- Bitwise operators
- Using the math module
- Booleans
- Relational operators
- Boolean logic operators
- Operator precedence
- Strings
- Other built-in types

---
layout: two-cols
---
# Numbers

Python has three numeric types
- Integers
- Floating point numbers
- Complex numbers

::right::

```python
i1 = 12345
i2 = 1234567890123456789
i3 = int("123", 8)
print("%d %d %d" % (i1, i2, i3))

f1 = 1.23
f2 = 4.56e-34
f3 = 7.89e+34
f4 = float("123.45")
print("%g %g %g %g" % (f1, f2, f3, f4))

c1 = 1 + 2j
c2 = 3 - 4j
c3 = 5j
c4 = complex("6+7j")
print("%g + %gi" % (c1.real, c1.imag))
print("%g + %gi" % (c2.real, c2.imag))
print("%g + %gi" % (c3.real, c3.imag))
print("%g + %gi" % (c4.real, c4.imag))
```

---
layout: two-cols
---

# Numeric operators

Python supports the following operators on numbers
- x ** y
- pow(x, y)
- divmod(x, y)
- c.conjugate()
- complex(re, im)
- float(x)
- int(x)
- abs(x)

::right::

- +x
- -x
- x % y
- x // y
- x / y
- x * y
- x - y
- x + y

---

# Using the math module

<v-clicks>

The math module defines several useful mathematical constants and functions
For details, see https://docs.python.org/3.10/library/math.html 

Example

```python
import math

print(dir(math))

print("pi is %f" % math.pi)
print("360 degrees in radians is %g" % math.radians(360))
print("2 * pi radians in degrees is %g" % math.degrees(2 * math.pi))

print("sin(90 degrees) is %.4f" % math.sin(math.pi / 2))
print("cos(90 degrees) is %.4f" % math.cos(math.pi / 2))
print("acos(0) is %g degrees" % math.degrees(math.acos(0)))

print("hypoteneuse of right-angled triangle (sides 3, 4) is %g" % math.hypot(3, 4))
print("5 factorial is %g" % math.factorial(5))
```

</v-clicks>

---

# Booleans

<v-clicks>

Boolean is a built-in type
- Represents truth or falsehood

The following values are considered false:
- None
- False
- Zero of any numeric type, e.g.  0, 0.0, 0j
- Any empty sequence, e.g. '', (), []
- Any empty mapping, e.g. {}

All other values are considered true
- Including the True keyword ☺

</v-clicks>

---

# Relational operators

Python supports the following relational operators
- <
- <=
- \>
- \>=
- ==
- !=
- is
- is not

---

# Boolean logic operators

Python has three boolean logic operators:
- not
- and
- or

Example

```python
month = int(input("Enter a month number [1-12]: "))

is_summer = month >=6 and month <= 8
is_winter = month == 12 or month == 1 or month == 2
is_transition_season = not(is_winter or is_summer)

print("%s %s %s" % (is_summer, is_winter, is_transition_season))
```

---

# Operator precedence

[This table shows the precedence of all operators from highest to lowest](https://docs.python.org/3/reference/expressions.html#operator-precedence)

---

# Strings

<v-clicks>

A string is an immutable sequence of Unicode characters

Can enclose in single quotes, double quotes, or triple quotes

```python
str1 = "The computer says 'No' I'm afraid."
str2 = '<a href="www.bbc.co.uk">Click here for the BBC</a>'

str3 = """Birthday present ideas:
 - Bugatti Chiron
 - 4xHD OLED 64-inch TV
 - Socks"""

print("%s\n%s\n%s" % (str1, str2, str3))
```

The String class defines many methods 
For details, see https://docs.python.org/3.10/library/string.html 

There's also excellent support for regular expressions

For details, see https://docs.python.org/3.10/library/re.html 

</v-clicks>

---

# Other built-in types

Text sequence types
- String - see previous slide

Basic sequence types
- List, tuple, and range

Binary sequence types
- bytes, bytesarray, and memoryview

Set types
- set, frozenset

Mapping type
- dict

---

# Any questions?

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

---


# Functions

---

- Getting started with functions
- Going further with functions

---

# Getting started with functions

- Simple functions
- Passing arguments to a function
- Returning a value from a function
- Understanding scope

---

# Simple functions (1/2)

<v-clicks>

A function is a named block of code
- Starts with the def keyword
- Followed by the name of the function
- Followed by parentheses, where you can define arguments
- Followed by a block, where you define the function body

```python
def name_of_function(arg1, arg2, …, argn):
  statements
  statements
  …
```

To call a function
- Specify the function name
- Followed by parentheses, where you can pass arguments

```python
name_of_function(argvalue1, argvalue2, …, argvaluen)
```

</v-clicks>

---
layout: two-cols
---
# Simple functions (2/2)


Here's an example of how to define and call simple functions

::right:: 

```python {all|1-4|1|2-4|6-9|11-12|1-12|15-18|20-21|all}
def say_goodmorning():
  print("Start of say_goodmorning")
  print(" Good morning!")
  print("End of say_goodmorning\n")

def say_goodafternoon():
  print("Start of say_goodafternoon")
  print("  Good afternoon!")
  print("End of say_goodafternoon\n")

def say_goodevening():
  pass


# Usage (i.e. client code)
say_goodmorning()
say_goodafternoon()
say_goodevening()

f = say_goodmorning
f()                   # Calls say_goodmorning() really

print("THE END")
```


---

# Passing arguments to a function

<v-clicks>

You can pass arguments to a function
- In the function definition, declare the argument names in the parentheses
- In the client code, pass argument values in the call

Example

```python {all|1-3|1-3,6|1-3,7|all}
def display_message(message, count):
  for i in range(count):
    print(message)

# Usage (i.e. client code)
display_message("Hello", 3)
display_message("Goodbye", 1)
```

</v-clicks>

---
layout: two-cols
---
# Returning a value from a function

Functions can return a value, via a return statement
- If you don't return a value explicitly, the function returns None

::right::

Example:

```python {all|1-2,15-16|4-5,18-19|7-11,21-22|all}
def display_message(msg):
  print(msg)

def generate_hyperlink(href, text):
  return "<a href='{0}'>{1}</a>".format(href, text)

def get_number_in_range(msg, lower, upper):
  while True:
    num = int(input(msg))
    if num >= lower and num < upper:
      return num


# Usage (i.e. client code)
result1 = display_message("Hello world")
print("result1 is %s" % result1)

result2 = generate_hyperlink("http://www.bbc.co.uk", "BBC")
print("result2 is %s" % result2)

result3 = get_number_in_range("Favourite month? ", 1, 13)
print("result3 is %s" % result3)
```

---

# Understanding scope (1/2)

<v-clicks>

If you declare a variable outside a function:
- The variable is global to the module
- Prefix the name with __ to make it private to this module

If you declare a variable inside a function:
- The variable is local to the function

If you want to assign a global variable inside a function:
- You must declare the variable inside the function, using the global keyword
- Tells the Python interpreter it's an existing global name, not a new local name

</v-clicks>

---

# Understanding scope (2/2)

This example shows how to define and use global variables

```python {all|1|4|6|11,14|all}
__DBNAME = None

def initDB(name):
  global __DBNAME
  if __DBNAME is None: 
    __DBNAME = name
  else:
    raise RuntimeError("Database name has already been set.")

def queryDB():
  print("TODO, add code to query %s" % __DBNAME)

def updateDB():
  print("TODO, add code to update %s" % __DBNAME)


# Usage (i.e. client code)
initDB("Server=.;Database=Northwind")
queryDB()
updateDB()
```

---

# Going further with functions

- Default argument values
- Variadic functions
- Passing keyword arguments 
- Variadic keyword arguments 
- Built-in functions
- Examples of using functions

---

# Default argument values

<v-clicks>

You can define default argument values for a function
- In the function definition, specify default values as appropriate
- In the client code, pass argument values or rely on defaults

Example:

```python {all|1|1,7|1,8|1,9|all}
def book_flight(fromairport, toairport, numadults=1, numchildren=0):
  print("\nFlight booked from %s to %s" % (fromairport, toairport))
  print("Number of adults: %d" % numadults)
  print("Number of children: %d" % numchildren)

# Usage (i.e. client code)
book_flight("BRS", "VER", 2, 2)
book_flight("LHR", "VIE", 4)
book_flight("LHR", "OSL")
```

</v-clicks>

---

# Variadic functions

<v-clicks>

Python allows you to define a function that can take any number of arguments
- In the function definition, prefix the last argument name with *
- Internally, these arguments will be wrapped up as a tuple
- You can iterate through the tuple items by using a for loop

Example

```python {all|1|1,7|3-4,7|}
def display_favourite_things(name, *things):
  print("Favourite things for %s" % name)
  for item in things:
    print("  %s" % item)

# Usage (i.e. client code)
display_favourite_things("Kath", "Ethan", "Caleb", 3, "Reading", "Learning", "Climbing")
```

</v-clicks>

---

# Passing keyword arguments 

<v-clicks>

Client code can pass arguments by name
- Use the syntax argument_name = value

Useful if the function has a lot of default argument values
- Client code can choose exactly which arguments to pass in

Example:

```python {all|1|1,7|1,8|1,9|all}
def book_flight(fromairport, toairport, numadults=1, numchildren=0):
  print("\nFlight booked from %s to %s" % (fromairport, toairport))
  print("Number of adults: %d" % numadults)
  print("Number of children: %d" % numchildren)

# Usage (i.e. client code)
book_flight("BRS", "VER", 2, 2)
book_flight("LHR", "CDG", numchildren=2)
book_flight(numchildren=3, fromairport="LGW", toairport="NCE")
```
</v-clicks>

---

# Variadic keyword arguments 

<v-clicks>

It's also possible to define variadic keyword arguments
- Use ** rather than * on the argument
- Allows you to pass in any number of keyword args

Internally, the arguments are wrapped as a dictionary
- You can iterate through the key/value pairs by using a for loop

Example

```python {all|1|1,6|2,3,6|all}
def myfunc(**kwargs):
  for k, v in kwargs.items(): 
    print ("key %s, value %s" % (k, v)) 

# Usage (i.e. client code)
myfunc(favTeam="Ireland", favNum=3, favColour="green")
```

</v-clicks>

---


# Built-in functions

[Python has a suite of built-in functions that are always available](https://docs.python.org/3/library/functions.html)

---

# Examples of Using Function (1/2)

I've written some examples to illustrate how to use functions in realistic scenarios
- Processing lines of text from a file
- Using regular expressions to find particular values in the file

Demo location
Demos\04-Functions\WorkedExamples


---

# Examples of using functions (2/2)

To open and read a file:
- Call open() to open a file - returns a file handle
- To read lines from the file, simply iterate over the file handle

To use regular expressions:
- The re module has compile() and search() functions to compile and use a regular expression

Here's the first example:

```python
import re

pattern = re.compile('Attribute ID \(0xC2\)')

with open('data.txt') as fh:
    for line in fh:
        result = pattern.search(line)
        if result:
            print(line)
```

---

# Any questions?

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

.

Basic sequence types
- List, tuple, and range

Text sequence types
- String

Binary sequence types
- bytes, bytesarray, and memoryview

---
layout: two-cols
---

# Lists

There are several ways to create a list
- []
- [item, item, item … ]
- list()
- list(iterable)

::right::

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

<v-clicks>

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

</v-clicks>

---
layout: two-cols
---

# Tuples

There are several ways to create a tuple
- ()
- a, or (a,)
- a,b,c or (a,b,c)
- tuple()
- tuple(iterable)

::right::

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
layout: two-cols
---

# Ranges

To create a range, use the range constructor
- range(stop)
- range(start, stop)
- range(start, stop, step)

::right::

Example:

```python {all|6|7|8|all}
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

```python {all|1,2|1,4|1,5|1,2,6|2,7|2,8|1,9|1,10|1,11|1,12|1,13|1,14|1,15|all}
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


```python {all|1,4|1,5|1,6|1,7|1,8|all}
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

<v-clicks>

You can unpack (i.e. extract) elements in a sequence

The following example illustrates the techniques available

```python {all|1,4,5|1,8,9|1,12,13|all}
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

</v-clicks>

---

# Sequence modification operations

You can perform these operations on a mutable sequence such as a list:

```python {all|3|4|5|6|7|1-8|10|11|12|8-13|15|16|13-17|19|20|21-22}
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
layout: two-cols
---

# Exercise

Write a Python program as follows:
- Ask the user to enter a series of numbers (-1 to quit)
- Determine which numbers are prime
- Display the prime numbers on the console

For the solution code:
See Solutions\05-DataStructures\primes.py

::right::

Here are more detailed instructions for this exercise:

1. Write a function named get_numbers().
   The function should loop around, asking the user to enter a number.
   For each number, add it to a list.
   Stop looping when the user enters -1.
   Return the list at the end of the function.
   
2. Write a function named find_primes().
   The function takes one argument - a list of numbers.
   The function should loop through the numbers, to find the prime numbers.
   The function should return the prime numbers.

3. Write a function named display_numbers().   
   The function takes one argument - a list of numbers.
   The function displays the numbers on the screen.

Call these functions from your "main" code, to get numbers from the user, find which ones are prime, and then print the prime numbers. 

---

# 3. Set Types

- Creating a set
- Creating a frozen set
- Common set operations
- Set modification operations

---
layout: two-cols
---

# Creating a set

There are several ways to create a set
- {item, item, item, … }
- set()
- set(iterable)
- Via a comprehension, similar to lists

::right::

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
layout: two-cols
---

# Creating a frozen set

Creating a frozenset is similar to creating a set
- Use the frozenset constructor

::right::

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

```python {all|1-3|5|6|1,2,7|1,3,8|1,2,9|1,2,10|1,2,11|1,2,12|1,2,13|1,2,14|1,2,3,15|1,2,3,15,16|1,2,3,17|17,18,1,2,3|1,2,19|1,2,20|all}
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

```python {all|6|7|}
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
layout: two-cols
---

# Creating a dictionary

There are several ways to create a dict
- {key:value, key:value, … }
- dict()
- dict(anotherDict)
- dict(keyword=value, keyword=value, … )
- dict(zip(keysIterable, valuesIterable))

::right::

Example:

```python
dict1 = {"us":"+1", "nl":"+31", "no":"+47"}
dict2 = dict()
dict3 = dict({"us":"+1", "nl":"+31", "no":"+47"})
dict4 = dict(us="+1", nl="+31", no="+47")
dict5 = dict(zip(["us", "nl", "no"], ["+1", "+31", "+47"]))

print("dict1 has %d items: %s" % (len(dict1), dict1))
print("dict2 has %d items: %s" % (len(dict2), dict2))
print("dict3 has %d items: %s" % (len(dict3), dict3))
print("dict4 has %d items: %s" % (len(dict4), dict4))
print("dict5 has %d items: %s" % (len(dict5), dict5))
```

---
layout: two-cols
---

# Iterating over a dictionary

There are several ways to iterate over a dict
- Iterate over the items (i.e. key-value pairs)
- Iterate over the keys
- Iterate over the values

::right::

Example:

```python
dialcodes = {"us": "+1", "nl": "+31", "no": "+47"}

print("Items:")
for k,v in dialcodes.items():
    print(k, v)

print("\nKeys:")
for k in dialcodes.keys():
    print(k)
    
print("\nValues:")
for v in dialcodes.values():
    print(v)
```

---

# Accessing items in a dictionary 

There are various operations for accessing items in a dict

```python
dialcodes = {"us": "+1", "nl": "+31", "no": "+47", "it": "+39"}

print("%s" % "us" in dialcodes)          # True
print("%s" % "us" not in dialcodes)      # False

dialcodes["uk"] = "+44"
print(dialcodes["uk"])                   # +44
print(dialcodes.get("fr"))               # None
print(dialcodes.get("fr", "xxx"))        # xxx

del dialcodes["no"]
print(dialcodes.pop("uk"))               # +44
print(dialcodes.pop("uk", "xxx"))        # xxx
print(dialcodes.setdefault("it", "???")) # ???

dialcodes.update({"ca":"+1", "it":"+39"}) 
print(dialcodes)  # {'ca': '+1', 'us': '+1', 'nl': '+31'}
```

---

# 5. Additional Techniques

- Generators
- List comprehensions
- Set comprehensions
- Dictionary comprehensions
- Filtering, sorting, and mapping
- Working with JSON data

---
layout: two-cols
---

# Generators

A generator is a special kind of function that returns a collection, one item at a time
- Use the yield keyword to yield the next value on each call

Example - consider the following two functions
- The 1st version returns a collection "all at once"
- The 2nd version yields a collection one element at a time

::right::

```python
def getNums():
    nums = []
    while True:
        num = int(input("Number? "))
        if num == -1 :
            break
        nums.append(num)
    return nums

# Client code.
nums = getNums()
for n in nums:
    print("  %d" % n)
```
```python
def getNumsB():
     while True:
        num = int(input("Number? "))
        if num == -1 :
            break
        yield num



# Client code.
nums = getNums()
for n in nums:
    print("  %d" % n)
```

---
layout: two-cols
---

# List comprehensions

You can create a list from another sequence
- Apply an operation on all the items in an existing sequence
- This is known as a "list comprehension"

::right::

Example:

```python
squares = [x**2 for x in range(6)]

ftemps = [32, 68, 212]
ctemps = [(f-32)*5/9 for f in ftemps]

print("squares: %s" % squares)
print("ftemps:  %s" % ftemps)
print("ctemps:  %s" % ctemps)
```

---
layout:two-cols
---

# Set comprehensions

You can also create a "set comprehension"
- i.e. a set created from another sequence


Example:

```python
ftemps = range(0, 50, 5)
ctemps = { int((f-32)*5/9) for f in ftemps }

print("ctemps:  %s" % ctemps)
```

---

# Dictionary comprehensions

You can also create a "dictionary comprehension"
- i.e. a collection of key/value pairs created from another sequence

Example:

```python
mydict = { i : i*i for i in range(1, 6) }

print("mydict:  %s" % mydict)
```

---
layout: two-cols
---

# Filtering, sorting, and mapping (1/2)

Python defines functions that allow you to filter, sort, and map (i.e. transform) the elements in a collection

Example

```python
names = ["Zak", "Tim", "Ben", "Joe", "Kim", "Bud", "Ted", "Baz"]

bnames = list(filter(startsWithB, names))
print(bnames)

sortedBnames = sorted(bnames)
print(sortedBnames)

mappedSortedBnames = list(map(topAndTail, sortedBnames))
print(mappedSortedBnames)
```

::right::

```python
def startsWithB(element):
  if len(element) and element[0] == 'B':
    return True
  else:
    return False
```

```python
def topAndTail(element):
    return "***" + element + "***"
```

---

# Filtering, sorting, and mapping (2/2)

The sorted() function takes two optional arguments, which allow you to take control over the sorting 
- key - function that indicates what aspect to sort items on
- reverse - boolean (default is false, i.e. ascending order)

Example

```python
names = ["Kevin", "Jayne", "Em", "Tom"]

sortedNamesAlphabetically = sorted(names)
print(sortedNamesAlphabetically)

sortedNamesByLength = sorted(names, key=personNameLength)
print(sortedNamesByLength)

sortedNamesByLengthDescending = sorted(names, key=personNameLength, reverse=True)
print(sortedNamesByLengthDescending)
```

---

# Working with JSON data (1/3)

JSON is a popular string data format
- Typically used for passing data to/from REST services
- Very easy to read/write JSON data in JavaScript (and in Python ☺)

Here are some example JSON strings:

```python
personJson = '{ "name": "Kevin", "age": 21, "height": 1.67, "isWelsh": true }'
coordsJson = '[ { "x": 100, "y": 150 }, { "x": 200, "y": 250 } ]'
```

To read/write JSON data in Python, use the standard Python module named json
- json.loads() loads JSON data into a Python dictionary/list
- json.dumps() dumps a Python dictionary/list into a JSON string

---

# Working with JSON data (2/3)

These examples show how to load JSON data into Python data structures

```python
import json

personJson = '{"name": "Kevin", "age": 21, "height": 1.67, "isWelsh": true }'

person = json.loads(personJson)

print("%s is %d years old" % (person["name"], person["age"]))
print("Height is %.2f, Welshness is %s" % (person["height"], person["isWelsh"]))
```


```python
import json

coordsJson = '[ { "x": 100, "y": 150 }, { "x": 200, "y": 250 } ]'

coords = json.loads(coordsJson)

print("Point 0 is %d, %d" % (coords[0]["x"], coords[0]["y"]))
print("Point 1 is %d, %d" % (coords[1]["x"], coords[1]["y"]))
```

Also see readJsonFromFile.py and sampledata.json

---

# Working with JSON data (3/3)

These examples show how to dump Python data into a JSON string

```python
import json

person = {"name": "Kevin", "age": 21, "height": 1.67, "isWelsh": True }

personJson = json.dumps(person, indent=4)  

print(personJson)
```

```python
import json

coords = [ { "x": 100, "y": 150 }, { "x": 200, "y": 250 } ]

coordsJson = json.dumps(coords, indent=4)  

print(coordsJson)
```

---

# Any questions?

---


# Object Oriented Programming (OOP)

---

- Essential concepts
- Defining and using a class
- Class-wide members

---

# Essential concepts

- What is a class?
- What is an object?
- Class diagrams

---

# What is a class?

<v-clicks>
 
A class is a representation of a real-world entity
- Defines data, plus methods to work on that data
- You can hide data from external code, to enforce encapsulation

Domain classes
- Specific to your business domain
- E.g. BankAccount, Customer, Patient, MedicalRecord

Infrastructure classes
- Implement technical infrastructure layer
- E.g. NetworkConnection, AccountsDataAccess, IPAddress

Error classes
- Represent known types of error
- E.g. Error, BankError, CustomerError

</v-clicks>

---

# What is an Object?

<v-clicks>

An object is an instance of a class
- Created (or "instantiated") by client code
- Each object is uniquely referenced by its memory address (no need for primary keys, as in a database)

Object management
- Objects are allocated on the garbage-collected heap
- An object remains allocated until the last remaining object reference disappears
- At this point, the object is available for garbage collection
- The garbage collector will reclaim its memory sometime thereafter

</v-clicks>

---
layout: image-right
image: ./assets/diagram.png
---

# Class Diagrams

During OO analysis and design, you map the real world into candidate classes in your application.


---

# Defining and using a class

- General syntax for class declarations
- Creating objects
- Defining and calling methods
- Defining instance variables
- Initialization methods
- Making an object's attributes private
- Implementing method behaviour

---

# General syntax for class declarations

<v-clicks>

General syntax for declaring a class:

```python
class ClassName :
  # 
  # Define attributes (data and methods) here.
  #
```

Example:

```python
class BankAccount :
  # 
  # Define BankAccount attributes (data and methods) here.
  #
```

</v-clicks>

---

# Creating objects

<v-clicks>

To create an instance (object) of the class:
- Use the name of the class, followed by parentheses
- Pass initialization parameters if necessary (see later)
- You get back an object reference, which points to the object in memory

```python
objectRef = ClassType(initializationParams)
```

Example

```python
from accounting import BankAccount

acc1 = BankAccount()
acc2 = BankAccount()
```

</v-clicks>

---

# Defining and calling methods

<v-clicks>

You can define methods in a class
- i.e. functions that operate on an instance of a class

In Python, methods must receive an extra first parameter
- Conventionally named self
- Allows the method to access attributes in the target object

```python
class BankAccount :
  def deposit(self, amount):
    print("TODO: implement deposit() code")

  def withdraw(self, amount):
    print("TODO: implement withdraw() code")
```



Client code can call methods on an object

```python
acc1 = BankAccount()
acc1.deposit(200)
acc1.withdraw(50)
```

</v-clicks>

---

# Initialization methods (1/2)

<v-clicks>

You can implement a special method named `__init__()`
- Called automatically by Python, whenever a new object is created
- The ideal place for you to initialize the new object!
- Similar to constructors in other OO languages

Typical approach:
- Define an `__init__()` method, with parameters if needed
- Inside the method, set attribute values on the target object
- Perform any additional initialization tasks, if needed

Client code:
- Pass in initialization values when you create an object

</v-clicks>

---

# Initialization methods (2/2)

<v-clicks>

Here's an example of how to implement `__init__()`

```python
class BankAccount:

    def __init__(self, accountHolder="Anonymous"):
        self.accountHolder = accountHolder
        self.balance = 0.0
    
    …
```

This is how client code creates objects now

```python
acc1 = BankAccount("Fred")
acc2 = BankAccount("Wilma")
```

</v-clicks>

---

# Making an object's attributes private

<v-clicks>

One of the goals of OO is encapsulation
- Keep things as private as possible

However, attributes in Python are public by default
- Client code can access the attributes freely!

```python
acc1 = BankAccount("Fred")
print("acc1 account holder is %s" % acc1.accountHolder)
```

To make an object's attributes private:
- Prefix the attribute name with two underscores, `__`

```python
class BankAccount:

    def __init__(self, accountHolder="Anonymous"):
        self.accountHolder = accountHolder
        self.__balance = 0.0
    
    …
```

</v-clicks>

---

# Implementing method behaviour

Here's a more complete implementation of our class

```python
class BankAccount:
    """Simple BankAccount class"""
    
    def __init__(self, accountHolder="Anonymous"):
        self.accountHolder = accountHolder
        self.__balance = 0.0

    def deposit(self, amount):
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        self.__balance -= amount
        return self.__balance

    def toString(self):
        return "{0}, {1}".format(self.accountHolder, self.__balance)
```

---

# Class-wide members

- Class-wide variables
- Class-wide methods
- @classmethod and @staticmethod

---

# Class-wide variables (1/2)

<v-clicks>

Class-wide variables belong to the class as a whole
- Allocated once, before usage of first object
- Remain allocated regardless of number of objects

To define a class-wide variable:
- Define the variable at global level in the class

```python
class BankAccount:
    __nextId = 1
    __OVERDRAFT_LIMIT = -1000
    …
```

To access the class-wide variable in methods:
- Prefix with the class name

</v-clicks>

---

# Class-wide variables (2/2)

Here's an example that puts it all together

```python
class BankAccount:
    
    __nextId = 1
    __OVERDRAFT_LIMIT = -1000


    def __init__(self, accountHolder="Anonymous"):
        self.accountHolder = accountHolder
        self.__balance = 0.0
        self.id = BankAccount.__nextId
        BankAccount.__nextId += 1


     def withdraw(self, amount):
        newBalance = self.__balance - amount
        if newBalance < BankAccount.__OVERDRAFT_LIMIT:
            print("Insufficient funds to withdraw %f" % amount)
        else:
            self.__balance = newBalance
        return self.__balance

    …
```

---

# Class-wide methods

<v-clicks>

Typical uses for class-wide methods:
- Get/set class-wide variables
- Factory methods, responsible for creating instances
- Instance management, keeping track of all instances

Example:

```python
class BankAccount:
    
    __nextId = 1
    __OVERDRAFT_LIMIT = -1000
    …

    def getOverdraftLimit():
        return BankAccount.__OVERDRAFT_LIMIT
```

Client code:

```python
print("Overdraft limit for all accounts is %d" % BankAccount.getOverdraftLimit())
```

</v-clicks>

---

# @classmethod and @staticmethod

<v-clicks>

The @classmethod and @staticmethod decorators can be applied to class-wide methods

```python
class BankAccount:

    __OVERDRAFT_LIMIT = -1000
    …

    @classmethod		
    def getOverdraftLimit(cls):
        return cls.__OVERDRAFT_LIMIT

    @staticmethod		
    def getBanner():
        return "\nThis is the BankAccount Banner"
```

```python
# Invoking via the class
print(BankAccount.getBanner())
print(BankAccount.getOverdraftLimit())

# Invoking via an instance
acc1 = BankAccount("Luke")
print(acc1.getBanner())
print(acc1.getOverdraftLimit())
```

</v-clicks>

---

# Any questions?

---


# Exceptions

---

- Getting started with exceptions
- Additional exception techniques

---

# Getting started with exceptions

- Overview
- Standard exceptions in Python
- Simple exception example
- Accessing the exception object

---

# Overview

<v-clicks>

Exceptions are a run-time mechanism for indicating exceptional conditions in Python
- If you detect an "exceptional" condition, you can throw an exception
- An exception is an object that contains relevant error info

Somewhere up the call stack, the exception is caught and dealt with
- If the exception is not caught, your application terminates

</v-clicks>

---

# Standard exceptions in Python

<v-clicks>

There are lots of things that can go wrong in a Python app
- Therefore, there are lots of different exception classes
- Each exception class represents a different kind of problem

Here are some of the standard exception classes in Python:
- KeyboardInterrupt
- OSError 
- EOFError
- ValueError
- … etc.

</v-clicks>

---

# Simple exception example

<v-clicks>

Here's a simple example of how to deal with exceptions in a Python app
- The try block contains code that might cause an exception
- The except block catches a particular type of exception

```python
# Keep on looping until the user enters a number.

while True:
    	
    try:
        inp = input("What's your favourite number? ")
        num = int(inp)
        print("Thanks, your favourite number is %d" % num)
        break
		
    except ValueError:
        print("Eek, that's not valid a number!")
```

</v-clicks>

---

# Accessing the exception object

<v-clicks>

In your except clause, you can specify a name for the exception object you just caught
- Allows you to use the exception object in your except block

Example 
- Catch ValueError and display error message on console

```python
# Keep on looping until the user enters a number.
while True:
    try:
        inp = input("What's your favourite number? ")
        num = int(inp)
        print("Thanks, your favourite number is %d" % num)
        break
		
    except ValueError as err:
        print("ValueError occurred: %s" % err)
```

</v-clicks>

---

# 2. Additional Exception Techniques

- Catching multiple exception types
- The "all ok" scenario
- Unconditional "wrap-up" code
- Exception hierarchies
- Defining custom exception classes
- Raising exceptions

---

# Catching multiple exception types (1/2)

<v-clicks>

If your try block contains complex code, then multiple different types of exception might occur
- You can define multiple except blocks, to catch each type of error
- Optionally the last except block can be a catch-all (omit the type)

Example

```python
import sys

try:
    fh = open('favNum.txt')
    str = fh.readline()
    num = int(str.strip())
    print("The number in the file is %d" % num)
	
except OSError as err:
    print("OSError occurred: %s" % err)

except ValueError as err:
    print("ValueError occurred: %s" % err)

except:
    print("Some other error occurred")
```

</v-clicks>

---

# Catching multiple exception types (2/2)

<v-clicks>

If you want to perform the same processing for several types of exception:
- Group the exceptions together in a single except block
- Specify the exception types as a tuple

```python
import sys

try:
    fh = open('favNum.txt')
    str = fh.readline()
    num = int(str.strip())
    print("The number in the file is %d" % num)
	
except (OSError, ValueError) as err:
    print("Error occurred: %s" % err)

except:
    print("Some other error occurred")
```

</v-clicks>

---

# The "all ok" scenario

<v-clicks>

You can add an else block at the end of try…except
- Executed only if the try block completed successfully 

```python
import sys

try:
    fh = open('favNum.txt')
    str = fh.readline()
    num = int(str.strip())
    print("The number in the file is %d" % num)
	
except OSError as err:
    print("OSError occurred: %s" % err)
…

else:
    print("All completed OK!")
    fh.close()	
```

</v-clicks>

---

# Unconditional "wrap-up" code

<v-clicks>

You can add a finally block at the end of everything
- Always executed at the end of the try…except…else construct
- Whether an exception occurred or not

```python
import sys

try:
    fh = open('favNum.txt')
    str = fh.readline()
    num = int(str.strip())
    print("The number in the file is %d" % num)
	
except OSError as err:
    print("OSError occurred: %s" % err)
…

else:
    print("All completed OK!")
    fh.close()	
	
finally:
    print("That's all folks. This message will always appear!")
```

</v-clicks>

---

# Exception hierarchies (1/2)

<v-clicks>

Python organizes exceptions into an inheritance hierarchy
- Represents specializations of general error conditions

Example
- There are several subclasses of OSError

- BaseException
    - Exception
        - OSError
            - FileNotFoundError
            - FileExistsError
            - PermissionError
            - ChildProcessError

</v-clicks>

---

# Exception hierarchies (2/2)

<v-clicks>

When you define an except block…
- It will catch that exception type, plus any subclasses

Example:
- "Special" processing for FileNotFoundError exceptions
- "Generic" processing for any other kind of OSError exceptions

```python
import sys

try:
    fh = open('favNum.txt')
    str = fh.readline()
    num = int(str.strip())
    print("The number in the file is %d" % num)
	
except FileNotFoundError as err:
    print("File not found: %s" % err)

except OSError as err:
    print("More general OSError occurred: %s" % err)

… plus other except blocks and an else block, as appropriate …
```

</v-clicks>

---

# Defining custom exception classes

<v-clicks>

You can define custom exception classes
- To represent important types of error in your application

How to do it:
- Define a class that inherits from Exception (or a subclass)
- Implement `__init__` and `__str__` methods

Example:

```python
class MyError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
```

</v-clicks>

---

# Raising exceptions

<v-clicks>

To raise (i.e. trigger) an exception:
- Use the raise keyword
- Specify the type of exception you want to raise
- Pass in any constructor arguemnts as appropriate

Example:

```python
try:
    raise MyError("EEK ERROR ERROR ERROR")
	
except MyError as err:
    print("It appears my exception occurred, the value is %s" % err.value)	
```

</v-clicks>

---

# Any questions?

---


# Bonus

---

- Sharing modules/packages with friends

---

# Sharing modules/packages with friends

- virtualenv
- requirements.txt
- Freezing
- Installing

---

# virtualenv

These can be managed within PyCharm or manually yourself.

It's probably best to allow PyCharm to do the heavy lifting here.

---

# requirements.txt

You can see the list of currently installed 3rd party packages with

```bash
pip freeze
```

To share this with someone else, conventionally we save this to a text file:

```bash
pip freeze > requirements.txt
```

and store this text file in source control.

---

# Installing from requirements.txt

<v-clicks>

To install from a requirements file, make sure you have the right virtualenv setup.

If necessary, create a new one with PyCharm or the command line tool.

Install the dependencies with:

```bash
pip install -r requirements.txt
```

Run the code as normal.

Note: This will synchronise the requirements but will still need you and your colleague to have a compatible version of the Python interpreter running.

</v-clicks>

---


# More Object Oriented Programming (OOP)

---

- A closer look at attributes
- Implementing magic methods
- Inheritance
- Help documentation
- Copying object state
- Reading/writing objects to a file

---

# A closer look at attributes

- Determining an object's attributes
- Adding and removing object attributes
- Built-in class attributes

---

# Determining an object's attributes

Python provides several global functions that allow you to manage attributes on an object

```python
from accounting import BankAccount

acc1 = BankAccount("Fred")

setattr(acc1, "bonus", 2000)

if hasattr(acc1, "bonus"):
    print("acc1.bonus is %d" % acc1.bonus)

delattr(acc1, "bonus")
```

---

# Adding and removing object attributes

You can also add and remove attributes on an object directly, as follows:

```python
from accounting import BankAccount

acc1 = BankAccount("Fred")

# Add an attribute to an object.
acc1.flag = "Whao watch this guy"     
print("acc1.flag is %s" % acc1.flag)

# Remove an attribute from an object.
del acc1.flag
```

---

# Built-in class attributes

Every class provides metadata via the following built-in attributes
- You can also get metadata about an object too

```python
from accounting import BankAccount

print("BankAccount.__doc__:",    BankAccount.__doc__)
print("BankAccount.__name__:",   BankAccount.__name__)
print("BankAccount.__module__:", BankAccount.__module__)
print("BankAccount.__bases__:",  BankAccount.__bases__)
print("BankAccount.__dict__:",   BankAccount.__dict__)

acc1 = BankAccount("Ola")
print("acc1.__dict__:", acc1.__dict__)
```

---

# Implementing magic methods

- Overview
- Implementing constructors and destructors
- Implementing stringify methods
- Implementing operator methods

---

# Overview

There are various "special" methods you can implement in your Python classes
- These methods allow your class objects to take advantage of standard Python idioms

It's good practice to implement these methods where relevant
- Python programmers will recognise these methods immediately
- Makes your classes easier to maintain

---

# Implementing constructors and destructors

Constructor
- `__init__(self, otherArgs)`

Destructor
- `__del__(self)`

Example

```python
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("In __init__() for %s and %d" % (self.name, self.age))

    def __del__(self):
        print("In __del__() for %s and %d" % (self.name, self.age))

p1 = Person("Bill", 23)
p2 = Person("Ben", 25)
…
del p1, p2
```

---

# Implementing stringify methods

Return a machine-readable representation of an object
- `__repr__(self)`

Return a human-readable representation of an object
- `__str__(self)`

Example

```python
class Person:

    def __repr__(self):
        return "{0} instance, name: {1}, age: {2}".format( \
                                                      self.__class__.__name__,\
                                                      self.name, self.age)
    def __str__(self):
        return "{0} is {1}.".format(self.name, self.age)
    …

print(repr(p1))
print(str(p2))
```

---

# Implementing operator methods

There are a large number of method that represent standard operators, including:
- `__eq__(self, other)`
- `__ne__(self, other)`
 Etc…

Example

```python
class Person:

    def __eq__(self, other):
        return self.age == other.age

    def __ne__(self, other):
        return self.age != other.age

    …

…

print("p1 == p2 gives %s" % (p1 == p2))
print("p1 != p2 gives %s" % (p1 != p2))
```

---

# Inheritance

- Overview of inheritance
- Superclasses and subclasses
- Sample hierarchy
- Defining a subclass
- Adding new members
- Defining constructors
- Overriding methods
- Multiple inheritance

---

# Overview of inheritance

<v-clicks>

Inheritance is a very important part of object-oriented development
- Allows you to define a new class based on an existing class
- You just specify how the new class differs from the existing class

Terminology:
- For the "existing class": 	Base class, superclass, parent class
- For the "new class":	Derived class, subclass, child class

Potential benefits of inheritance:
- Improved OO model
- Faster development
- Smaller code base

</v-clicks>

---

# Superclasses and subclasses

The subclass inherits everything from the superclass (except constructors)
- You can define additional variables and methods
- You can override existing methods from the superclass
- You typically have to define constructors too
- Note: You can't cherry pick or "blank off" superclass members

---

# Sample hierarchy

We'll see how to implement the following simple hierarchy:


BankAccount <- SavingsAccount

Note:
- BankAccount defines common state and behaviour that is relevant for all kinds of account
- SavingsAccount "is a kind of" BankAccount that earns interest

We might define additional subclasses in the future…
- E.g. CurrentAccount, a kind of BankAccount that has cheques

---

# Defining a subclass

To define a subclass, use the following syntax
- Note that a Python class can inherit from multiple superclasses
- We'll discuss multiple inheritance later in this chapter

```python
class Subclass(Superclass1, Superclass2, …) : 

    # Additional attributes and methods …

    # Constructor(s) …

    # Overrides for superclass methods, if necessary …
```

Example:
```python
class SavingsAccount(BankAccount):
    …
    …
    …
```

---

# Adding new members

The subclass inherits everything from the superclass
- (Except for constructors)
- The subclass can define additional members if it needs to …

Example:

```python
class SavingsAccount(BankAccount):

    __DEFAULT_INTEREST_RATE = 1.5


    def earnInterest(self):
        self.balance *= (1 + self.interestRate)
        return self.balance 

    …
```

---

# Defining constructors

A subclass doesn't inherit the constructor from superclass
- So, define a constructor in the subclass, to initialize subclass state

The subclass constructor should invoke the superclass constructor, to initialize superclass data
- Call `super().__init__(params)`

Example:

```python
class SavingsAccount(BankAccount):

    def __init__(self, accountHolder="Anonymous", interestRate=None):

        super().__init__(accountHolder)

        if interestRate is None:
            self.interestRate = SavingsAccount.__DEFAULT_INTEREST_RATE
        else:
            self.interestRate = interestRate
    …
```

---

# Overriding methods

The subclass can override superclass instance methods
- To provide a different (or supplementary) implementation
- No obligation ☺

An override can call the original superclass method, to leverage existing functionality
- Call super().methodName(params)

Example:

```python
class SavingsAccount(BankAccount):

    def withdraw(self, amount):
        if amount > self.balance:
            print("You can't go overdrawn in a savings account!")
        else:
            super().withdraw(amount)
        return self.balance    
    …
```

---

# Multiple inheritance (1/2)

Python supports multiple inheritance

```python
class Logger:
    def log(self, msg):
        print(msg)

class Beeper:
    def beep(self, duration):
        winsound.Beep(2500, duration)
```

```python
class Alerter(Logger, Beeper):
    def doShortAlert(self, msg):
        super().log(msg)
        super().beep(250)

    def doMediumAlert(self, msg):
        super().log(msg)
        super().beep(1000)

    def doLongAlert(self, msg):
        super().log(msg)
        super().beep(2500)
```

---

# Multiple inheritance (2/2)

Client code can access public members in the subclass or in any superclass

```python
alerter = Alerter()

alerter.log("Wakey wakey!")
for i in range(30):
    alerter.beep(50)

msg = input("Enter an alert message: ")
alerter.doShortAlert(msg)

msg = input("Enter another alert message: ")
alerter.doMediumAlert(msg)

msg = input("And another: ")
alerter.doLongAlert(msg)
```
---

# Help documentation

You can provide "help" documentation at the start of the class and the start of each method
- Define a help string  """like this"""
- For an example, see accounting2.py

You can then get help for the class or methods via the help() function in the Python shell

---

# Copying object state

When you assign one object reference to another:
- It just copies the object reference
- So both references refer to the same actual object

If you want to create a copy of an object:
- Call the copy() function, defined in the copy module

Example:
See demoCopying.py

---

# Reading/writing objects to a file

A common requirement is to read/write objects to a file

There are various ways to do this in Python:
- As JSON 
- As XML
- As CSV

You can also write your own custom code
See accounting3.py, clientcodeReadWriteObjects.py

---

# Any questions?

---


# Functional Programming

---

- Functional programming in Python
- Higher order functions
- Additional techniques

---

# 1. Functional Programming in Python

- Overview of functional programming (FP)
- Function evaluation
- Pure functions
- Anonymous functions a.k.a. lambdas
- Lambda example
- Lambdas and parameters

---

# Overview of functional programming (FP)


<v-clicks>

FP is a style of programming characterised by…
- Treating computation as the evaluation of functions
- Use of higher-order functions and/or recursion
- Immutable (read-only) state
- Lazy evaluation

Why use FP?
- Very amenable to multi-threading
- Share complex algorithms across multiple threads, to maximise concurrency and increase performance

Any disadvantages?
- Quite a steep learning curve
- Not suitable for every problem

</v-clicks>

---

# Function evaluation

<v-clicks>

Functions depend only on their inputs, and not on other program state

For example, consider the following function

```python
def cube(x):
  return x * x * x
```

It always gives the same answer for the same input (so it has predictable behaviour - you can reason about its operation)

It has no local state, side-effects, or changes to any other program state (so it can be safely executed by multiple threads)

</v-clicks>

---

# Pure functions

A "pure function" is one that has no side effects. This has several useful consequences:

<v-clicks>

- If the result of a pure expression is not used, it can be removed without affecting anything else

- If a pure function is called with the same arguments, you will get the same result (so evaluations can be cached)

- If there is no data dependency between two pure functions, they can be evaluated in any order, or performed in parallel

</v-clicks>

---

# Anonymous functions a.k.a. lambdas

<v-clicks>

A lambda expression is a 1-line inline expression
- Like an anonymous function

To define a lambda expression:
- Use the lambda keyword
- Followed by the argument list
- Followed by a colon
- Followed by a 1-line inline expression

```python
my_lambda = lambda arg1, arg2, … argn  :  inline_expression
```

To invoke a lambda expression:
- Same syntax as a regular function call

```python
my_lambda(argvalue1, argvalue2, …, argvaluen)
```

</v-clicks>

---

# Lambda example

A lambda that takes a single parameter and returns the square of that value

```python
mylambda = lambda x: x * x

result = mylambda(10)
print(result)
```

---

# Lambdas and parameters

<v-clicks>

Lambdas can take multiple parameters
- List all the parameters after the lambda keyword

```python
mylambda = lambda x, y: print(f"You passed {x}, {y}")
mylambda(10, 20)
```

Lambdas can take no parameters
- Just follow the lambda keyword with a : immediately

```python
mylambda = lambda: print("Hello!")

mylambda()
```

</v-clicks>

---

# 2. Higher Order Functions

- Overview of higher-order functions
- Passing a lambda to a function
- Returning a lambda from a function
- Closures

---

# Overview of higher-order functions

<v-clicks>

Higher-order functions can use other functions as arguments and return values
- You can pass a function as a parameter into another function
- You can return a function from a function

We'll explore both these techniques in the following slides
- We'll use lambdas to represent the function parameters/returns

</v-clicks>

---

# Passing a lambda to a function

<v-clicks>

You can pass a lambda as a parameter into a function
- Allows you to write very generic functions

Example
- The apply() function applies the lambda that you pass in

```python
def apply(arg1, arg2, op) :
    return op(arg1, arg2)

result1 = apply(10, 20, lambda x, y: x + y)
print(result1)

result2 = apply(10, 20, lambda x, y: x / y)
print(result2)
```

</v-clicks>

---

# Returning a lambda from a function

<v-clicks>

You can return a lambda from a function

Consider this simple concat() function
- Concatenates its two parameters in the order specified

```python
def concat(str1, str2):
    return str1 + str2
```

Now consider the flip() function
- Takes a binary operation 
- Returns a lambda that performs the operation with args flipped

```python {all|2|1,2,5|6|all}
def flip(binaryOp) :
    return lambda x, y: binaryOp(y, x)

# Usage.
flipConcat = flip(concat)
result2 = flipConcat("Hello", "World")
print(result2)
```

</v-clicks>

---

# Closures (1/2)

<v-clicks>

A closure is a function whose behaviour depends on variables declared outside the scope in which it is then used
- This is often used when returning functions/lambdas
- The returned function/lambda remembers the original state in the enclosing function

```python {all|1|2|4|6,7,2|all}
def banner(start, end) :
    return lambda msg: print(f"{start} {message} {end}")

bannerMsg = banner("[---", "---]")

bannerMsg("Hello")
bannerMsg("World")
```

</v-clicks>

---

# Closures (2/2)

<v-clicks>

Here, fib returns a function that calculates Fibonacci numbers, returns the next one each time called

```python {all|2|4|5|6|8|all}
def fib():
    tup = (1,-1)
    def retfunc():
        nonlocal tup
        tup = (tup[0] + tup[1], tup[0])
        return tup[0]

    return retfunc
```

Note 1: 
nonlocal keyword lets you access a variable in external scope

Note 2:
tup is a tuple, and you access its members using [0] and [1]

</v-clicks>

---

# 3. Additional Techniques

- Recursion
- Tail recursion
- Reduction
- Partial functions

---

# Recursion

Recursion is commonly used instead of looping
- It avoids the mutable state associated with loop counters

```python {all|2|4,5|2|4,5|2|all}
def factorial(n):
    if n == 0:
        return 1
    else: 
        return n * factorial(n - 1)
```

```python
result = factorial(4)
print("4 factorial is %d\n" % result)
```

---

# Tail Recursion

Tail recursion is where the very last thing you do in a function is call yourself
- The function calls can theoretically be executed in a simple loop

Here's a tail-recursive implementation of factorial

```python
def tailRecursiveFactorial(accumulator, n):
    if n == 0:
        return accumulator
    else: 
        return tailRecursiveFactorial(n * accumulator, n - 1)

result = tailRecursiveFactorial(1, 4)
print("4 factorial is %d\n" % result)
```

---

# Reduction

The functools module has several useful utility functions for functional programming
- E.g. reduce(), which reduces the elements in a collection to a single result

```python
from functools import reduce

mylambda = lambda x,y: x+y

result = reduce(mylambda, [3,12,19,1,2,7])
print(result)
```

---

# Partial Functions

<v-clicks>

The functools module also allows you to create partial functions, i.e. functions with one or more args already filled in
- Via partial()

```python
from functools import partial

multiply = lambda x,y: x * y

times2 = partial(multiply, 2)
times5 = partial(multiply, 5)
times8 = partial(multiply, 8)

print("10 times 2 is %d" % times2(10))
print("10 times 5 is %d" % times5(10))
```

Note: If you're interested to learn how this works, see our own version of partial() here:
- PartialFunctionsHowTheyWork.py

</v-clicks>

---

# Any Questions?

---


# Decorators

---

1. Getting started with decorators
2. Additional decorator techniques
3. Parameterized decorators

---

# 1. Getting started with decorators

- Overview
- Defining a decorator function
- Applying a decorator function manually
- Applying a decorator function properly

---

# Overview

<v-clicks>

Python allows you to decorate functions and classes using the @decorator syntax

The decorator enhances the function/class with extra capabilities

```python
@someDecorator
def someFunction(…) :
   …
```

```python
@someDecorator
class SomeClass :
   …
```

This section shows how to define decorators
- We'll see how to define decorator functions
- We'll also describe how Python applies decorator functions

</v-clicks>

---
layout: two-cols
---

# Defining a decorator function (1/2)

<v-clicks>

Define a function that takes a function pointer as an argument
- The pointer indicates the target function you want to decorate

Inside the decorator function, implement a nested function 
- The nested function should call the target function
- And should also perform the desired decoration behaviour

At the end of the decorator function, return a pointer to the nested function 

</v-clicks>

::right::

<div v-click="4">

```python {all|1|4-7|10|all}
def simpleDecorator(func) :

    # Define an inner function, which wraps (decorates) the target function.
    def innerFunc() :
        print("Start of simpleDecorator()")    
        func()
        print("End of simpleDecorator()")
   
    # Return the inner function.
    return innerFunc
```

</div>

---
layout: two-cols
---

# Applying a decorator function manually

<v-clicks>

In order to understand how decorators work, let's first of all see how to apply a decorator function manually:


Line 6 calls the decorator function manually, passing a pointer to the target function as an argument
- This statement returns a pointer to the inner function

Line 7 calls the inner function
- This invokes the target function, with the desired decoration

</v-clicks>

::right::


```python {all|6|7|all}
# Some function that we want to decorate.
def myfunc1() :
    print("Hi from myfunc1()")

# Client code.
pointerToInnerFunc = simpleDecorator(myfunc1)    
pointerToInnerFunc()                             
```

---

# Applying a decorator function properly

<v-clicks>

The previous slide showed how to call a decorator function manually, to wrap a target function

Now let's see how to apply a decorator function properly, i.e. using the @decorator syntax

```python
# Some function, which we now decorate explicitly.
@simpleDecorator
def myfunc1() :
    print("Hi from myfunc1()")

# Client code.
myfunc1()
```

Note the client code just calls myfunc1() directly
- Python intervenes, thanks to the @simpleDecorator decorator, and converts the code to the equivalent of the previous slide

</v-clicks>

---

# Additional decorator techniques

- Decorating a function that takes arguments
- Decorating a function that returns a result

---

# Decorating a function that takes arguments

<v-clicks>

Consider the following function, which takes arguments
Note that we've decorated the function

```python
@parameterAwareDecorator
def myfunc1(firstName, lastName, nationality) :
    print(f"Hi {firstName} {lastName}, your nationality is {nationality}")
```

This is how to define the decorator function
- The inner function receives variadic args and passes to target func

```python
def parameterAwareDecorator(func) :

   def innerFunc(*args, **kwargs) :
        print("Start of parameterAwareDecorator()")    
        func(*args, **kwargs)
        print("End of parameterAwareDecorator()")
   
   return innerFunc
```

Client code:

```python
myfunc1("Ola", "Nordmann", "Norsk")
myfunc1(nationality="Cymraeg", lastName="Cunningham", firstName="Jayne")
```

</v-clicks>

---

# Decorating a function that returns a result

<v-clicks>

Consider the following function, which returns a result

```python
@returnAwareDecorator
def myfunc1(firstName, lastName, nationality) :
    return f"Hi {firstName} {lastName}, your nationality is {nationality}"
```

This is how to define the decorator function
- The inner function returns the result of the target function

```python {all|5|7|all}
def returnAwareDecorator(func) :

    def innerFunc(*args, **kwargs) :
        print("Start of returnAwareDecorator()")    
        returnValueFromFunc = func(*args, **kwargs)
        print("End of returnAwareDecorator()")
        return returnValueFromFunc
        
    return innerFunc
```

Client code:

```python
res1 = myfunc1("Kari", "Nordmann", "Norsk")
res2 = myfunc1(nationality="Cymraeg", lastName="Cunningham", firstName="Kevin")
```

</v-clicks>

---

# Parameterized decorators

- Overview
- Defining a parameterized decorator
- Applying a parameterized decorator manually
- Applying a parameterized decorator properly

---

# Overview

<v-clicks>

Decorators can take parameters, to make them flexible

E.g. imagine a flexible decorator that displays custom pre/post messages around a target function call
- You might apply the decorator as follows
- The decorator takes parameters specifying the pre/post messages

```python
@parameterizedDecorator("HELLO", "GOODBYE")
def myfunc1(firstName, lastName, nationality) :
    return "Hi %s %s, your nationality is %s" % (firstName, lastName, nationality)
```

</v-clicks>

---
layout: two-cols
---
# Defining a Parameterized Decorator

Here's how to define a parameterized decorator

```python {all|1|3-16|4|7-11|13|16|all}
def parameterizedDecorator(prefix, suffix) :

    # Define inner function, which just wraps a function.
    def innerFunc1(func) :
    
        # Define inner-inner function, which decorates/calls target function.
        def innerFunc2(*args, **kwargs) :
            print(prefix)    
            returnValueFromFunc = func(*args, **kwargs)
            print(suffix)
            return returnValueFromFunc
            
        # Return innerFunc2, i.e. the inner-inner function.    
        return innerFunc2
        
    # Return innerFunc1, i.e. the inner function.
    return innerFunc1
```

::right::

We have a layering of functions, to handle all the args:
- Arguments to the decorator itself
- The target function to be invoked
- Arguments to pass in to the target function

---
layout: two-cols
---
# Applying a Parameterized Decorator Manually 


In order to understand how parameterized decorators work, let's first see how to apply the decorator manually:

```python {all|6|7|8|all}
# Some function, which we don't decorate explicitly here.
def myfunc1(firstName, lastName, nationality) :
    return "Hi %s %s, your nationality is %s" % (firstName, lastName, nationality) 
  
# Client code
pointerToInnerFunc1 = parameterizedDecorator("HELLO", "GOODBYE")  
pointerToInnerFunc2 = pointerToInnerFunc1(myfunc1)                
res = pointerToInnerFunc2("Per", "Nordmann", "Norsk")            
```



::right::

<v-clicks>

Line 6 calls the decorator manually, passing args into it
- This statement returns a pointer to innerFunc1

Line 7 calls innerFunc1, passing target function into it
- This just return a pointer to innerFunc2

Line 8 calls innerFunc2, passing args for the target func
- This invokes the target func, with the desired decoration

</v-clicks>

---

# Applying a Parameterized Decorator Properly

<v-clicks>

The previous slide showed how to call a parameterized decorator function manually, to wrap a target function

Now let's see how to apply a parameterized decorator function properly, i.e. using the @decorator syntax


```python
# Some function, which we now decorate explicitly.
@parameterizedDecorator("HELLO", "GOODBYE")
def myfunc1(firstName, lastName, nationality) :
    return "Hi %s %s, your nationality is %s" % (firstName, lastName, nationality)

# Client code.
res1 = myfunc1("Kari", "Nordmann", "Norsk")
```

Note the client code just calls myfunc1() directly
- Python intervenes, thanks to the @parameterizedDecorator, and cascades through the necessary sequence of function calls and argument-passing


</v-clicks>

---

# Any questions?

---


# Asynchronous Processing in Python

---

1. Getting started with asynchrony in Python
2. Managing coroutines via tasks
3. Additional task techniques

---

# Getting started with asynchrony in Python

- Overview
- Asynchrony in Python
- Coroutines
- The asyncio module
- Simple example of asynchrony

---

# Overview

<v-clicks>

What is asynchrony?
- The ability to perform multiple tasks concurrently

Scenarios where asynchrony is important:
- Processing a large dataset in parallel
- Handling multiple network connections simultaneously
- Performing algorithmic processing in the background
- Etc.

</v-clicks>

---

# Asynchrony in Python

<v-clicks>

You can schedule concurrent tasks on a single thread
- The event loop manages task execution on a thread

The event loop can optimize I/O
- If a function is waiting on I/O
- The event loop pauses the function and runs another one instead
- When the first function completes I/O, it is resumed

The event loop can also optimize CPU-intensive functions
- The functions must explicitly "yield", so as not to hog the thread

Note: Python also supports genuine multithreading
- See multipleThreadsAndFutures.py

</v-clicks>

---

# Coroutines

<v-clicks>

A coroutine is a special kind of generator function 
- It can cede control during its processing (e.g. for I/O)
- The event loop then tries to give another coroutine some time
- The event loop can resume the original coroutine when it's ready

The preferred way to define a coroutine in modern Python is to prefix a function with the async keyword

```python
async def someFunc(someArgs) :
    # Some long-running code that might yield control
    #   e.g. code that does slow I/O
    #   e.g. code that CPU-intensive processing
```

</v-clicks>

---

# The asyncio module

<v-clicks>

The asyncio module provides various methods that allow you to schedule and manage asynchrony
- Some of the common methods are listed here

asyncio.sleep(seconds)
- Sleep for a specified delay (in seconds)

asyncio.run(aCoroutine)
- Creates a new event loop, and runs the coroutine

asyncio.create_task()
- Schedule a coroutine to be executed "soon" on the event loop

</v-clicks>

---
layout: two-cols
---

# Simple example of asynchrony

```python
import asyncio
from time import strftime, localtime

async def displayAfter(msg, delay) :
    await asyncio.sleep(delay)
    now = strftime("%H:%M:%S", localtime())
    print("%s %s" % (now, msg))
    
def main():
    print("*****Start of main*****")
    asyncio.run(displayAfter("Hei", 3))
    asyncio.run(displayAfter("Bye", 5))
    print("*****End of main*****")
    
if __name__ == "__main__" :
    main()
```

::right::

<v-clicks>

- asyncio.sleep() is a coroutine
- The await keyword yields control back to the event loop, which  tries to schedule other coroutines in the meantime
- You can only use the await keyword in coroutines, i.e. functions  marked as async
- You can't just 'invoke' coroutines, you must schedule via asyncio

</v-clicks>

---

# Managing coroutines via tasks

- Overview
- Simple example of creating a task
- Creating and awaiting multiple tasks
- Awaiting multiple tasks to complete

---

# Overview

<v-clicks>

The asyncio.create_task() function creates a task 
- The task is scheduled for execution "soon" on the event loop
- The task is represented by a Task object

The Task class has methods that allow you to manage the running of the task, such as:
- done()   - has the task completed yet?
- cancel() - stop the task now
- result() - get the result of the task (it must have finished!)

</v-clicks>

---

# Simple example of creating a task 

```python
from time import strftime, localtime
import asyncio

def doDisplay(msg):
    now = strftime("%H:%M:%S", localtime())
    print("%s %s" % (now, msg))

async def displayAfter(msg, delay) :
    doDisplay("START: " + msg)
    await asyncio.sleep(delay)
    doDisplay("END: " + msg)
    
async def main():
    print("*****Start of main*****")
    task = asyncio.create_task(displayAfter("Hello", 10))
    
    for i in range(0,5) :
        print("Doing something useful...")
        await asyncio.sleep(1)
    
    print("Finished doing useful work, now I'll wait for task to finish")     
    await task
    print("*****End of main*****")
    
if __name__ == "__main__" :
    asyncio.run(main())
```

---
layout: two-cols
---

# Creating and awaiting multiple tasks

You can create multiple tasks
- All the tasks run concurrently
- You can await for each task to complete individually

::right::

```python
async def main():
    doDisplay("*****Start of main*****")
    task1 = asyncio.create_task(displayAfter("Bonjour", 10))
    task2 = asyncio.create_task(displayAfter("Bore da", 15))
    task3 = asyncio.create_task(displayAfter("Hei hei", 20))
    
    for i in range(0,5) :
        doDisplay("Doing something useful...")
        await asyncio.sleep(1)
    
    doDisplay("Waiting for task1 to finish")     
    await task1

    doDisplay("Waiting for task2 to finish")     
    await task2

    doDisplay("Waiting for task3 to finish")     
    await task3

    doDisplay("*****End of main*****")
```

---

# Awaiting multiple tasks to complete

The previous example awaited individual tasks to complete
- If you prefer, you can await multiple tasks to complete
- Use asyncio.gather(), which suspends until all tasks are done

```python
async def main():
    doDisplay("*****Start of main*****")
    task1 = asyncio.create_task(displayAfter("Bonjour", 10))
    task2 = asyncio.create_task(displayAfter("Bore da", 15))
    task3 = asyncio.create_task(displayAfter("Hei hei", 20))
    
    for i in range(0,5) :
        doDisplay("Doing something useful...")
        await asyncio.sleep(1)
    
    doDisplay("Waiting multiple tasks to complete")     
    await asyncio.gather(task1, task2, task3)

    doDisplay("*****End of main*****")
```

---

# Additional task techniques

- Awaiting the result of a task
- Polling a task to see if it's done
- Cancelling a task

---

# Awaiting the result of a task (1/2)

<v-clicks>

A coroutine can return a value
- The calling code would like to retrieve the value when complete

Here's one way for the calling code to do this:
- Create a task, to schedule the coroutine for execution
- Await completion of the task 
- The await expression gives the result of the completed coroutine

```python
async def createStringAfter(msg, delay) :
    await asyncio.sleep(delay)
    now = strftime("%H:%M:%S", localtime())
    return "{0} {1}".format(now, msg)
    
async def main():
    print("*****Start of main*****")
    task = asyncio.create_task(createStringAfter("Bonjour", 10))
    result = await task
    print(result)
    print("*****End of main*****")
```

</v-clicks>

---

# Awaiting the result of a task (2/2)

<v-clicks>

The previous slide created a task, and then awaited its completion separately:

```python
async def main():
    print("*****Start of main*****")
    task = asyncio.create_task(createStringAfter("Bonjour", 10))
    result = await task
    print(result)
    print("*****End of main*****")
```

If it's more convenient, you can combine these two statements into a single statement

```python
async def main():
    print("*****Start of main*****")
    result = await asyncio.create_task(createStringAfter("Bonjour", 10))
    print(result)
    print("*****End of main*****")
```

</v-clicks>

---

# Polling a task to see if it's done

Sometimes you might want to poll a task to see if it's done
- Call done() on the task, to see if it's finished
- If it hasn't finished, do something else for a bit, then check again
- When it really has finished, call result() on the task

```python
async def main():
    doDisplay("*****Start of main*****")
    task = asyncio.create_task(createStringAfter("Bonjour", 10))
    
    while True: 
        if task.done():
            result = task.result()
            doDisplay(result)
            break
        else:
            doDisplay("Doing something useful...")
            await asyncio.sleep(1)

    doDisplay("*****End of main*****")
```

---

# Cancelling a task

Sometimes you might want to cancel a task mid-flight
- Call cancel() on the task

```python
async def main():
    doDisplay("*****Start of main*****")
    task = asyncio.create_task(createStringAfter("Bonjour", 10))
    
    while True: 
        if task.done():
            result = task.result()
            doDisplay(result)
            break
        else:
            cancel = input("Task not complete yet. Do you want to cancel it? ")
            if cancel == "y":
                doDisplay("OK I'll cancel the task and we'll all just move on in life.")
                task.cancel()
                break
            else:
                doDisplay("OK I'll wait another second and do something useful...")
                await asyncio.sleep(1)

    doDisplay("*****End of main*****")
```

---

# Any questions?

---


# Getting Started with NumPy

---

- Introduction to Python data science
- NumPy arrays 
- Manipulating array elements
- Manipulating array shape

---

# Introduction to Python data science

- Overview
- Python libraries for data science
- Getting the data science libraries

---

# Overview

<v-clicks>

Python is a popular choice for data science and machine learning

Attractive characteristics of Python:
- Dynamic language, so it's good for rapid exploratory coding
- Relatively simple syntax, so it's easier to become proficient
- Popular in schools and universities, so the skills are out there!

</v-clicks>

---

# Python libraries for data science

<v-clicks>

NumPy is a numeric processing API for Python
- Fast mathematical computation of numeric arrays and matrices

Pandas provides additional features based on NumPy
- Additional support for indexing, reading/writing CSV/Excel, etc.

Matplotlib is a graphical plotting API for Python
- Similar to Matlab, allows you to plot graphs, charts, etc.

Scikit-Learn is a machine learning library for Python
- Implements many supervised/unsupervised learning algorithms

</v-clicks>

---

# Getting the data science libraries

If you're using Anaconda, these are already downloaded for you.

If you're using a standalone Python distribution, you'll need to install the libraries you need.

```bash
pip install numpy

pip install openpyxl
pip install xlrd
pip install matplotlib

pip install pandas
```

---

# NumPy arrays 

- Getting Started with NumPy arrays
- Techniques for creating NumPy arrays
- Reading CSV data
- Visualizing data

---

# Getting Started with NumPy arrays (1/2)

<v-clicks>

NumPy holds data in N-dimensional arrays
- An array is an instance of the numpy.ndarray class
- https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.html

All the data in a NumPy array is the same type
- This allows NumPy to store and process the data efficiently
- This is a very important point!

Why are NumPy arrays more efficient than Python lists?
- Python is dynamically typed, so every object contains metadata that identifies the type at run time
- In a Python list, every item contains this metadata - eek!
- In a NumPy array, only the array itself contains the metadata

</v-clicks>

---
layout: two-cols
---

# Getting Started with NumPy arrays (2/2)

<v-clicks>

Example
- Creates a NumPy array from a Python list
- Gets the shape of the array, via the shape property 
- Gets the data type of array elements, via the dtype property

For a full list of NumPy standard types, see:
- https://numpy.org/devdocs/user/basics.types.html

</v-clicks>

::right::

```python {all|4|5|6|7}
import numpy as np

# Create a 1D NumPy array from a Python list.
a = np.array([1, 2, 3])
print('Data values in a\n', a)
print('Shape of a:', a.shape)
print('Data type in a:', a.dtype)

# Create a 2D Numpy array from a Python list of lists.
b = np.array([[1, 2, 3], [4, 5, 6]])
print('\nData values in b\n', b)
print('Shape of b:', b.shape)
print('Data type in b:', b.dtype)
```



---

# Techniques for creating NumPy arrays (1/2)

There are lots of ways to create a NumPy array

```python {all|3|4|5|6|7|8|9|10|all}
import numpy as np

a = np.array([1, 2, 3.14]) # Create array with mixed types - NumPy converts elements "upwards".
b = np.array([1, 2, 3], dtype='float64') # Create array with a specified type.
c = np.arange(0, 20, 2) # Create array from a numeric range.
d = np.linspace(0.0, 1.0, 11) # Create array of elements, linear spaced. 
e = np.zeros(5) # Create array of zeros. 
f = np.ones(5)   # Create array of ones.
g = np.full(5, 1.23) # Create array of elements, with specified value.
h = np.empty(5) # Create array of elements, no specified value.
```

---

# Techniques for creating NumPy arrays (2/2)

You can also create random arrays, which can be handy

```python
# Import the NumPy module. 
import numpy as np

# Create random values in range [0.0, 1.0).
a = np.random.random(10)

# Create normally-distributed random values.
b = np.random.normal(5, 2, 10)

# Create random integers in range [0, 101).
c = np.random.randint(0, 101, 10)
```

---

# Reading CSV data

<v-clicks>

A common requirement is to read data from a CSV file
- The easiest way to do this is via the Pandas read_csv() function

Pandas reads values into a multi-column DataFrame
- You can then extract a column into a NumPy array

```python
import numpy as np
import pandas as pd

# Read a csv file, get a Pandas DataFrame back.
dataframe = pd.read_csv('WorldCupWinners.csv')

# Get the 'Teams' column.
teams = np.array(dataframe['Team'])
print(teams)
```

We'll not have time to dive into Pandas on this course but it's a topic worth exploring!


</v-clicks>


---

# Visualizing data (1/2)

<v-clicks>

Visualization is an important aid to help you understand the shape and meaning of data

You can use the MatPlotLib library to visualize data in lots of different ways
- Line graphs
- Scatter graphs
- Bar-charts
- Pie-charts
- Histograms
- Etc.

</v-clicks>

---

# Visualizing data (2/2)

Here's a simple example of how to visualize data using MatPlotLib - we'll see more plotting features later

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = np.array([1, 19, 76, 45, 34, 42, 30, 5, 77, 54, 89])

plt.xlabel('Element in array')
plt.ylabel('Value')
plt.plot(data)
plt.show()
```

---

# Manipulating array elements

- Indexing into an array
- Slicing an array
- Accessing a specific column or row
- Aside: Views vs. copies

---
layout: two-cols
---

# Indexing into an array

Indexing into a NumPy array is quite intuitive
- [i]	Access element from start, first element is at [0]
- [-i]	Access element from end, last element is at [-1]
- [r,c]	Access element in 2-D array (etc. for higher dimensions)

::right::

```python
import numpy as np

# Create a 1-D array, index into it, and modify elements.
a = np.array([0, 10, 20, 30, 40, 50, 60, 70])
print(a)
print(a[1])        # 10
print(a[-1])       # 70
a[1] = 111
print(a)

# Create a 2-D array, index into it, and modify elements.
b = np.array([[0, 10, 20, 40], [50, 60, 70, 80]])
print(b)
print(b[0, 1])     # 10
print(b[0, -1])    # 40
print(b[-1, 1])    # 60
print(b[-1, -1])   # 80
b[0, 1] = 111
print(b)
```

---
layout: two-cols
---
# Slicing an array

You can slice into an array using a [start:stop:step] index
- start	Default start is 0
- stop	Default stop is the size of the dimension
- step	Default step is 1

::right::

```python
import numpy as np

# Create a 1-D array, and get various slices.
a = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80])
print(a[3:])         # [30 40 50 60 70 80]
print(a[:3])         # [ 0 10 20]
print(a[3:7])        # [30 40 50 60]
print(a[3:7:2])      # [30 50]
print(a[3::2])       # [30 50 70]
print(a[::2])        # [ 0 20 40 60 80]

# Create a 2-D array, and get various slices in each dimension.
b = np.array([[0, 10, 20], [30, 40, 50], [60, 70, 80]])
print(b[1:, 1:])     # [ [40 50] [70 80] ]
print(b[:2, :2])     # [ [ 0 10] [30 40] ]
print(b[::2, ::2])   # [ [ 0 20] [60 80] ]

# Etc :-)
```

---
layout: two-cols
---

# Accessing a specific column or row

To get a specific column or row in a multidimension array:
- Use an empty slice to skip a dimension
- E.g. in a 2D array, [:,1] gets column 1
- E.g. in a 2D array, [1,:] gets row 1

::right::

```python
import numpy as np

a = np.array([[0, 10, 20], [30, 40, 50], [60, 70, 80]])

# To access a specific column...
print(a[:, 0])   # [ 0 30 60]
print(a[:, 1])   # [10 40 70]
print(a[:, 2])   # [20 50 80]

# To access a specific row...
print(a[0, :])   # [ 0 10 20]
print(a[1, :])   # [30 40 50]
print(a[2, :])   # [60 70 80]

# To access a specific row, simpler syntax...
print(a[0])      # [ 0 10 20]
print(a[1])      # [30 40 50]
print(a[2])      # [60 70 80]
```

---
layout: two-cols
---

# Aside: Views vs. copies

When you get an array slice/row/column, you get a view on the data
- If you make any changes, it will change the actual data 

If you want to get a copy of the data:
- Call copy() on the slice/row/column

::right::

```python
import numpy as np

# Demonstrate views.
a = np.array([[0, 10, 20], [30, 40, 50], [60, 70, 80]])
col0View = a[:, 0]
col0View[2] = 600
print(col0View)
print(a)   # [[ 0  10  20] [ 30  40  50] [600  70  80]]

# Demonstrate copies.
b = np.array([[0, 10, 20], [30, 40, 50], [60, 70, 80]])
col0Copy = a[:, 0].copy()
col0Copy[2] = 600
print(col0Copy)
print(b)   # [[ 0  10  20] [ 30  40  50] [60  70  80]]
```

---

# Manipulating array shape

- Reshaping an array
- Creating new axes
- Concatenating arrays
- Stacking arrays vertically or horizontally
- Splitting an array

---
layout: two-cols
---

# Reshaping an array

Reshaping is a simple and common technique for creating multidimensional arrays
- Create a 1D array initially (typically)
- Reshape it to a multidimensional array (must be compatible shape)
- The multidimensional array is a view onto the original 1D array

::right::

```python
import numpy as np

# Create 1D array initially, for simplicity.
a = np.arange(9)
print(a)               # [0 1 2 3 4 5 6 7 8]
print(a.shape)         # (9,)

# Reshape as 2D array (view on a).
b = a.reshape((3,3))   
print(b)               # [[0 1 2] [3 4 5] [6 7 8]]
print(b.shape)         # (3, 3)

# Changing items in b will change values in underlying a.
b[0,0] = 99          
print(a)               # [99  1  2  3  4  5  6  7  8]
print(b)               # [[99  1  2] [ 3  4  5] [ 6  7  8]]
```

---

# Creating new axes

Another useful technique is create new axes for an array
- Create a 1D array initially (typically)
- Create a new column or row, using np.newaxis

```python
import numpy as np

# Create 1D array initially, for simplicity.
a = np.arange(5)
print(a)               # [0 1 2 3 4]
print(a.shape)         # (5,)

# Create 2D array with 1 row, 5 columns. 
b = a[np.newaxis, :]   
print(b)               # [[0 1 2 3 4]]
print(b.shape)         # (1, 5)

# Create 2D array with 5 rows, 1 column. 
c = a[:, np.newaxis]   
print(c)               # [[0] [1] [2] [3] [4]]
print(c.shape)         # (5, 1)
```

---

# Concatenating arrays (1/2)

You can concatenate same-size arrays together
- np.concatenate() - you can specify the axis to concatenate on 

Here's a simple example that concatenates 1D arrays

```python
import numpy as np

# Create some 1D arrays.
a = np.array([ 0,  1])
b = np.array([10, 11])
c = np.array([20, 21])

# Concatenate the 1D arrays.
result = np.concatenate([a, b, c])
print(result)         # [0 1 10 11 20 21]
print(result.shape)   # (6,) 
```

---

# Concatenating arrays (2/2)

Here's an example that concatenates 2D arrays
- Note the optional axis parameter (default is 0)

```python
import numpy as np

# Create some 2D arrays.
a = np.array([[ 0,  1], [10, 11]])
b = np.array([[20, 21], [30, 31]])
c = np.array([[40, 41], [50, 51]])

# Concatenate on axis 0 (this is the default, so can omit axis parameter).
result1 = np.concatenate([a, b, c], axis=0)
print(result1)         # [[0 1] [10 11] [20 21] [30 31] [40 41] [50 51]]
print(result1.shape)   # (6, 2)      

# Concatenate on axis 1.
result2 = np.concatenate([a, b, c], axis=1)
print(result2)         # [[0 1 20 21 40 41] [10 11 30 31 50 51]]
print(result2.shape)   # (2, 6) 
```

---

# Stacking arrays vertically or horizontally

You can stack different-size arrays together
- np.vstack() - stack vertically (must have same no. of cols)
- np.hstack() - stack horizontally (must have same no. of rows)

```python
import numpy as np

# Create some arrays with same number of columns (2), and stack vertically.
a = np.array([10, 11])
b = np.array([[20, 21], [30, 31]])
result1 = np.vstack([a, b])
print(result1)         # [[10 11] [20 21] [30 31]]
print(result1.shape)   # (3, 2)      

# Create some arrays with same number of rows (2), and stack horizontally.
c = np.array([[40, 41], [50, 51]])
d = np.array([[60], [61]])
result2 = np.hstack([c, d])
print(result2)         # [[40 41 60] [50 51 61]]
print(result2.shape)   # (2, 3) 
```

---
layout: two-cols
---

# Splitting an array

You can split an array into subarrays
- np.split()
- np.vsplit()
- np.hsplit()

::right::

```python
import numpy as np

# Split a 1D array.
a = np.arange(16)
a1, a2, a3, a4 = np.split(a, [2, 5, 9])
print('\na1\n', a1)   # [0 1] 
print('\na2\n', a2)   # [2 3 4] 
print('\na3\n', a3)   # [5 6 7 8]
print('\na4\n', a4)   # [9 10 11 12 13 14 15]

# Split a 2D vertically.
b = np.arange(16).reshape((4, 4))
b1, b2 = np.vsplit(b, [3])
print('\ntop\n', b1)     # [[0 1 2 3] [4 5 6 7] [8 9 10 11]] 
print('\nbottom\n', b2)  # [[12 13 14 15]]

# Split a 2D horizontally.
c = np.arange(16).reshape((4, 4))
c1, c2 = np.hsplit(c, [3])
print('\nleft\n', c1)    # [[0 1 2] [4 5 6] [8 9 10] [12 13 14]] 
print('\nright\n', c2)   # [[3] [7] [11] [15]]
```

---

# Any questions?

---


# NumPy Techniques

---

- NumPy universal functions
- Aggregation
- Broadcasting
- Manipulating arrays using Boolean logic
- Additional techniques

---

# NumPy universal functions

- Overview
- Using a loop
- Using a universal function
- Arithmetic
- Reduction and accumulation
- Additional math functions

---

# Overview

<v-clicks>

Universal functions are a key reason why NumPy arrays are so efficient to manipulate

A universal function is a method on a NumPy array that executes on all elements very efficiently
- Much faster and cleaner than using an explicit loop

Consider the examples on the next 2 slides…
- The 1st example uses a loop - slow and cumbersome
- The 2nd example uses a universal function - fast and elegant

You will always use universal functions rather than loops to process NumPy arrays

</v-clicks>

---

# Using a loop

This code uses a loop to process data in a NumPy array
- Loops through elements and applies ** to each element
- Gathers results into another NumPy array, one-by-one 

```python
import numpy as np
from timeit import default_timer as timer

def compute_cubes_loop(data):
    result = np.empty(len(data))
    for i in range(len(data)):
        result[i] = data[i] ** 3    
    return result

np.random.seed(0)
data = np.random.randint(1, 10, size=10_000_000)

start = timer()
cubes = compute_cubes_loop(data)
end = timer()
print('Execution time using a loop', end - start)
```

---

# Using a universal function

This code has the same effect, using a universal function 
- Applies the ** operator to the NumPy array itself
- NumPy applies the operator to each element implicitly

```python
import numpy as np
from timeit import default_timer as timer

def compute_cubes_ufunc(data):
    result = data ** 3
    return result

np.random.seed(0)
data = np.random.randint(1, 10, size=10000000)

start = timer()
cubes = compute_cubes_ufunc(data)
end = timer()
print('Execution time using a universal function', end - start)
```

---
layout: two-cols
---
# Arithmetic

NumPy implements all the usual arithmetic operators as universal functions 
- You can use an operator directly, or call the equivalent function

::right::

```python
import numpy as np

a = np.arange(10)

print('Using operators')
print('a + 2  = ', a + 2)
print('a - 2  = ', a - 2)
print('a * 2  = ', a * 2)
print('a / 2  = ', a / 2)
print('a // 2 = ', a // 2)
print('a % 2  = ', a % 2)
print('a ** 2 = ', a ** 2)

print('\nUsing ufuncs explicitly')
print('np.add(a, 2)          = ', np.add(a, 2))
print('np.subtract(a, 2)     = ', np.subtract(a, 2))
print('np.multiply(a, 2)     = ', np.multiply(a, 2))
print('np.divide(a, 2)       = ', np.divide(a, 2))
print('np.floor_divide(a, 2) = ', np.floor_divide(a, 2))
print('np.mod(a, 2)          = ', np.mod(a, 2))
print('np.power(a, 2)        = ', np.power(a, 2))
```

---

# Reduction and accumulation

For binary ufuncs such as add, multiply, etc.
- You can call reduce() to reduce array to a single result
- You can call accumulate() to accumulate intermediate results

```python
import numpy as np

a = np.arange(2, 5)

print('reduce() examples')
print('Sum    ', np.add.reduce(a))
print('Product', np.multiply.reduce(a))
print('Power  ', np.power.reduce(a))

print('accumulate() examples')
print('Sum    ', np.add.accumulate(a))
print('Product', np.multiply.accumulate(a))
print('Power  ', np.power.accumulate(a))
```

---
layout: two-cols
---

# Additional math functions

NumPy has universal functions for trig, log, etc.

::right::

```python
import numpy as np
import scipy.special as sp  # Additional specialized functions.

a = np.linspace(0, np.pi, 3)
print('sin(a)  = ', np.sin(a))
print('cos(a)  = ', np.cos(a))
print('tan(a)  = ', np.tan(a))
print('sinh(a) = ', np.sinh(a))
print('cosh(a) = ', np.cosh(a))
print('tanh(a) = ', np.tanh(a))

b = np.linspace(0.1, 0.9, 3)
print('arcsin(b)  = ', np.arcsin(b))
print('arccos(b)  = ', np.arccos(b))
print('arctan(b)  = ', np.arctan(b))
print('arcsinh(b) = ', np.arcsinh(b))
print('arccosh(b) = ', np.arccosh(b))
print('arctanh(b) = ', np.arctanh(b))

c = np.array([1, 10, 100])
print('log(c)   = ', np.log(c))       # 2.718281 to the power what gives c?
print('log2(c)  = ', np.log2(c))      # 2 to the power what gives c?
print('log10(c) = ', np.log10(c))     # 10 to the power what gives c?
print('exp(c)   = ', np.exp(c))       # 2.718281 to the power c
print('exp2(c)  = ', np.exp2(c))      # 2 to the power c
print('exp10(c) = ', sp.exp10(c))     # 10 to the power c
```

---

# Aggregation

- Overview
- NumPy vs. Python aggregation functions
- NumPy aggregation functions available
- Working with multidimensional arrays

---

# Overview

<v-clicks>

When dealing with large amounts of data, you'll probably want to compute statistics such as:
- Sum, product
- Minimum, maximum
- Mean, median, mode
- Variance, standard deviation
- Percentiles

NumPy has aggregation functions for performing these computations very efficiently

</v-clicks>

---

# NumPy vs. Python aggregation functions

NumPy aggregation functions look very similar to functions available in the standard Python library
- But the NumPy functions are much quicker, so use them!

Consider the following example:

```python {all|4|6-9|11-14|all}
import numpy as np
from timeit import default_timer as timer

data = np.random.rand(100_000_000)

start1 = timer()
result1 = sum(data)      # Python sum() function
end1 = timer()
print('Execution time using Python sum():  ', end1 - start1)

start2 = timer()
result2 = np.sum(data)   # NumPy sum() function
end2 = timer()
print('Execution time using NumPy sum(): ', end2 - start2)
```

---

# NumPy aggregation functions available

This example shows the NumPy aggregation functions
- There are also NaN-friendly functions, e.g. np.nansum()

```python
import numpy as np
from scipy import stats

data = np.random.rand(100_000_000)

print('Sum            ', np.sum(data))
print('Product        ', np.prod(data))
print('Minimum        ', np.min(data))
print('Maximum        ', np.max(data))
print('Mean           ', np.mean(data))
print('Median         ', np.median(data))
print('Mode           ', stats.mode(data))
print('Variance       ', np.var(data))
print('Std dev        ', np.std(data))
print('50th percentile', np.percentile(data, 50))
```

---

# Working with multidimensional arrays

<v-clicks>

The aggregation functions work over the entire array
- If the array is multidimensional, all elements are processed

You can also get aggregation results for rows or columns
- Specify the axis parameter, to collapse data on that axis

```python
import numpy as np

data = np.arange(9).reshape([3,3])

# Print the entire array.
print('Array data:\n', data)

# Calculate the sum over the entire array.
print('Sum of whole array:', np.sum(data))

# Collapse axis 0 (i.e. collapse the rows), to get sum on each column.
print('Sum for each column:', np.sum(data, axis=0))

# Collapse axis 1 (i.e. collapse the columns), to get sum on each row.
print('Sum for each row:', np.sum(data, axis=1))
```

</v-clicks>

---

# Broadcasting

- Universal functions and same-shape arrays
- Universal functions and different-shape arrays
- Broadcasting rules
- Understanding the broadcasting rules

---

# Universal functions and same-shape arrays

<v-clicks>

We discussed universal functions earlier in the chapter
- We showed how to add/subtract/etc. scalars to an array

```python
import numpy as np

a = np.array([0, 1, 2])

result = a + 100
print(result)
```

Universal functions also work with arrays for both args
In this example, the arrays are the same shape (3,)

```python
import numpy as np

a1 = np.array([0, 1, 2])
a2 = np.array([4, 5, 6])

result = a1 + a2
print(result)
```

</v-clicks>

---

# Universal functions and different-shape arrays

Universal functions also work with different-shape arrays
- This is called broadcasting - see next slide for details

Here's a simple example of broadcasting 
- a is one row, m is two rows
- The values in a are "broadcast" across both rows in m

```python
import numpy as np

a = np.array([10, 11, 12])
print(a.shape)       # (3,)

m = np.array([[20, 21, 22], [30, 31, 32]])
print(m.shape)       # (2,3)

result = a + m       
print(result.shape)  # (2, 3)
print(result)        # [[30 32 34] [40 42 44]]
```

---

# Broadcasting rules

<v-clicks>

Broadcasting allows NumPy to stretch arrays of different shapes, to enable binary operations to take place

There are three rules about how broadcasting works, which are applied in the following order:

1. If arrays have a different number of dimensions, the shape of the array with fewer dimensions is filled with 1 on leading edge

2. If shape of arrays is different in any dimension, the array with shape 1 in that dimension is stretched to match the other shape

3. If shape in any dimension is different (and not 1), an error occurs

</v-clicks>

---

# Understanding the broadcasting rules

<v-clicks>

Let's re-examine the example from a couple of slides ago

```python
a = np.array([10, 11, 12])
m = np.array([[20, 21, 22], [30, 31, 32]])
result = a + m     # [[30 32 34] [40 42 44]]  
```


Let's apply broadcasting rule 1 first…
- a and m have different number of dimensions: a is 1D, m is 2D
- a has fewer dimensions, so a shape is filled with 1 on leading edge
- Thus the shape of a becomes (1, 3) i.e. 1 row of 3 columns

Now let's apply broadcasting rule 2…
- a and m have different shapes: a shape is (1,3), m shape is (2,3)
- a shape (1,3) is stretched to match m shape (2,3)

</v-clicks>

---

# Complex Broadcasting

<v-clicks>

In this example, both arrays need to be broadcast

```python
import numpy as np

a = np.array([[10],[11],[12]])   # Shape (3,1)
b = np.array([20, 21, 22])       # Shape (3,)
result = a + b                   # Shape (3,3)
print(result)                    # [[30 31 32] [31 32 33] [32 33 34]]
```

Let's apply broadcasting rule 1 first…
- a and b have different number of dimensions: a is 2D, b is 1D
- b has fewer dimensions, so b shape is filled with 1 on leading edge
- Thus the shape of b becomes (1, 3) i.e. 1 row of 3 columns

Now let's apply broadcasting rule 2…
- a and b have different shapes: a shape is (3,1), b shape is (1,3)
- a cols stretched to match b cols, so a becomes (3,3)
- b rows stretched to match a rows, so b becomes (3,3)

</v-clicks>

---

# Manipulating arrays using Boolean logic

- Boolean operations
- Boolean aggregation
- Boolean masking

---

# Boolean operations (1/2)

<v-clicks>

We've seen how to use math operators with NumPy arrays
- `+ - * / // etc.`

You can also use Boolean operators
- `>  >=  <  <=  ==  !=  `
- Returns a NumPy array containing True/False in each position

```python
import numpy as np

def process_marks(m):
    print('Exam marks\n',      m)
    print('Passes?\n',         m >= 50)
    print('Full marks?\n',     m == 100)
    print('Not full marks?\n', m != 100)

my_exam_marks = np.array([71, 95, 49, 100, 65])
process_marks(my_exam_marks)

our_exam_marks = np.array([[71, 95, 49, 100, 65], [99, 23, 78, 88, 92]])
process_marks(our_exam_marks)
```

</v-clicks>

---

# Boolean operations (2/2)

You can combine Boolean operations together
- &  and
- |  inclusive or
- ^  exclusive or
- ~  not

```python
import numpy as np

def process_marks(m)
    print('\nExam marks\n',               m)
    print('B?\n',                       (m >= 60) & (m < 70))
    print('A or U?\n',                  (m >= 70) | (m < 30))
    print('A or even, but not both?\n', (m >= 70) ^ (m % 2 == 0))
    print('Not (A or U)?\n',            ~((m >= 70) | (m < 30)))

my_exam_marks = np.array([71, 95, 49, 100, 65])
process_marks(my_exam_marks)

our_exam_marks = np.array([[71, 95, 49, 100, 65], [99, 22, 78, 88, 92]])
process_marks(our_exam_marks)
```

Note the need for parentheses, for operator precedence

---

# Boolean aggregation

You can perform various aggregation operations on the Boolean result arrays
- all()           - are all results True? 
- any()           - are any results True?
- count_nonzero() - count of non-zero (i.e. True) results	

```python
import numpy as np

def process_marks(m)
    print('\nExam marks\n',  m)
    print('All passes?    ', np.all(m >= 50))
    print('Any passes?    ', np.any(m >= 50))
    print('Count of passes', np.count_nonzero(m >= 50))
    print('Count of B     ', np.count_nonzero((m >= 60) & (m < 70)))
    print('Count of A or U', np.count_nonzero((m >= 70) | (m < 30)))

my_exam_marks = np.array([71, 95, 49, 100, 65])
process_marks(my_exam_marks)

our_exam_marks = np.array([[71, 95, 49, 100, 65], [99, 22, 78, 88, 92]])
process_marks(our_exam_marks)
```

---
# Boolean masking

You can use a Boolean result matrix as a mask
- array[booleanTest]
- Yields all array elements that have a True Boolean result

```python
import numpy as np
def process_marks(m)
    print('\nPasses      ', m[m >= 50])
    print('B marks     ', m[(m >= 60) & (m < 70)])
    print('A or U marks', m[(m >= 70) | (m < 30)])

my_exam_marks = np.array([71, 95, 49, 100, 65])
process_marks(my_exam_marks)

our_exam_marks = np.array([[71, 95, 49, 100, 65], [99, 23, 78, 88, 92]])
process_marks(our_exam_marks)
```

---

# Additional techniques

- Fancy indexing
- Partitioning
- Sorting

---
layout: two-cols
---

# Fancy indexing (1/3)

Often you want to get several elements at specific indices
- You can pass an array of indices into []
- Returns a result array with the elements from those indices

::right::

```python
import numpy as np

a = np.arange(10, 20)

# Get some elements into a Python list.
result1 = [a[1], a[4], a[7]]
print('type(result1)', type(result1))
print('result1      ', result1)

# Get some elements into a NumPy array, using fancy indexing.
idx = [1, 4, 7]
result2 = a[idx]
print('\ntype(result2)', type(result2))
print('result2.shape',   result2.shape)
print('result2      ',   result2)

# Get some elements into a 2D NumPy array, using fancy indexing.
idx = np.array([[1, 4, 7], [2, 5, 8]])
result3 = a[idx]
print('\ntype(result3)', type(result3))
print('result3.shape',   result3.shape)
print('result3      ',   result3)
```

---

# Fancy indexing (2/3)

You can use fancy indexing with multidimensional arrays
- Specify a fancy index indicating desired rows
- Specify another fancy index indicating desired columns

```python
import numpy as np

a = np.arange(49).reshape(7,7)

# Use fancy indexing to specify rows and columns desired.
ridx = [0, 2, 4]
cidx = [1, 3, 5]
result = a[ridx, cidx]
print('result.shape', result.shape)
print('result      ', result)
```

---
layout: two-cols
---

# Fancy indexing (3/3)

You can combine fancy indexing with other techniques
- E.g. regular indexing, slicing, masking

::right::

```python
import numpy as np

a = np.arange(49).reshape(7,7)

# Combine fancy indexing with regular indexing.
cidx = [1, 3, 5]
result1 = a[2, cidx]
print('result1.shape', result1.shape)
print('result1\n',     result1)

# Combine fancy indexing with slicing.
cidx = [1, 3, 5]
result2 = a[2:5, cidx]
print('\nresult2.shape', result2.shape)
print('result2\n',       result2)

# Combine fancy indexing with masking.
rmask = [True, True, False, False, False, False, True]
cidx = [1, 3, 5]
result3 = a[rmask, cidx]
print('\nresult3.shape', result3.shape)
print('result3\n',       result3)
```

---
layout: two-cols
---
# Partitioning

<v-clicks>

You can partition an array via partition()
- You specify an index position, returns an array where all elements up to that position are smaller than all values after that position

Notes:
- Elements are unsorted within each partition
- For multidimensional arrays, the default axis of partitioning is 0
- There's also a partition() instance method, partitions in-place

</v-clicks>

::right::

```python
import numpy as np

a = np.random.randint(0, 101, 12)
print('Unpartitioned 1D array', a)
print('Partitioned at index 2', np.partition(a, 2))
print('Partitioned at index 4', np.partition(a, 4))

b = np.random.randint(0, 101, 49).reshape((7,7))
print('\nUnpartitioned 2D array\n', b)
print('\nPartitioned at col index 2\n', b.partition(2, axis=1))
print('\nPartitioned at col index 4\n', np.partition(b, 4, axis=1))
print('\nPartitioned at row index 2\n', np.partition(b, 2, axis=0))
print('\nPartitioned at row index 4\n', np.partition(b, 4, axis=0))
```


---

# Sorting

You can sort an array via sort()
Returns a sorted array

```python
import numpy as np

a = np.random.randint(0, 101, 12)
print('Unsorted 1D array', a)
print('Sorted           ', np.sort(a))

b = np.random.randint(0, 101, 49).reshape((7,7))
print('\nUnsorted 2D array\n', b)
print('\nSorted across cols\n', np.sort(b, axis=1))
print('\nSorted down rows  \n', np.sort(b, axis=0))
```

Notes:
- For multidimensional arrays, the default axis of partitioning is 0
- There's also a sort() instance method, sorts in-place
- There's also a sort() instance method, sorts in-place

---

# Any questions?

---


# Test Automation

---

- Getting started with testing
- Using PyHamcrest matchers
- Testing techniques

---

# Getting started with testing

- Setting the scene
- Python test frameworks
- Example class-under-test
- How to write a test
- Example test
- Running tests
- Arrange / Act / Assert
- Testing for exceptions
- Setup and teardown code

---

# Setting the scene

<v-clicks>

Unit testing verifies the correct behaviour of your code artefacts in isolation
- In Python, a "unit" is usually a function

You typically write several unit tests per function
- To exercise all the possible paths through the function

The FIRST principles of unit testing:
- Fast
- Isolated / independent
- Repeatable
- Self-validating
- Timely

</v-clicks>

---

# Python test frameworks

<v-clicks>

There are several test frameworks available for Python
- Unittest (aka PyUnit) - part of standard library (OO-based)
- PyTest - simple and fast, most widely used (function-based)
- TestProject - generates HTML reports, use with PyTest or Unittest
- Behave - BDD test framework
- Robot - primarily for Acceptance Testing
- Etc.

We'll use PyTest
- Install as follows:

```
pip install pytest
```

Test installation as follows:

```
py.test -h
```

</v-clicks>

---

# Example class-under-test

In the next few slides we'll see how to test this simple Python class

```python
class BankAccount:

    def __init__(self, name):
        self.name = name
        self.balance = 0;

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise Exception("Insufficient funds")
        self.balance -= amount

    def __str__(self):
        return "{}, {}".format(self.name, self.balance)

```

---

# How to write a test

<v-clicks>

To write tests in PyTest:
- Define a separate .py file 
- The filename must be test_xxx.py or xxx_test.py

Each test is a separate function
- The function name must be test_yyy()

Each test function should focus on a particular scenario, and should have a meaningful name
- E.g. test_functionName_Scenario
- E.g. test_functionName_StateUnderTest_ExpectedBehaviour

</v-clicks>

---

# Example test

<v-clicks>

When writing your tests, go for the low-hanging fruit first
- Test the simplest functions and scenarios first
- Then test the more complex functions and scenarios later

Here's a simple first test

```python
from bankAccount import BankAccount

def test_accountCreated_zeroBalanceInitially():
    fixture = BankAccount("David")
    assert fixture.balance == 0
```

Notes:
- assert is a standard Python keyword
- If the test returns false, it throws an AssertionError
- This causes your test function to terminate immediately

</v-clicks>

---

# Running tests

To run tests in PyTest, run the following command:

```
py.test
```

---

# Arrange / Act / Assert

<v-clicks>

It's common for a test function to have 3 parts
- Arrange
- Act
- Assert

Example

```python
def test_deposit_singleDeposit_correctBalance():

    # Arrange.
    fixture = BankAccount("David")

    # Act.
    fixture.deposit(100)

    # Assert.
    assert fixture.balance == 100
```

</v-clicks>

---

# Testing for exceptions (1/2)

<v-clicks>

When you write industrial-strength code, sometimes you actually want the code to throw an exception
- The code should be robust enough to detect exceptional situations
- You can write a test to verify the code throws an exception

```python
import pytest
…

def test_deposit_withdrawalsExceedLimits_exceptionOccursV1():

    # Arrange.
    fixture = BankAccount("David")

    # Act.
    fixture.deposit(600)

    # Verify expected exception occurs
    with pytest.raises(Exception):
        fixture.withdraw(601)

```

</v-clicks>

---

# Testing for exceptions (2/2)

If you want to examine the exception that was thrown:

```python
import pytest
…

def test_deposit_withdrawalsExceedLimits_exceptionOccursV2():

    # Arrange.
    fixture = BankAccount("David")

    # Act.
    fixture.deposit(600)

    # Verify expected exception occurs
    with pytest.raises(Exception) as excinfo:
        fixture.withdraw(601)

    # Assert the exception type and error message are correct
    assert excinfo.typename == "Exception"
    assert excinfo.value.args[0] == "Insufficient funds"

```

---

# Setup and teardown code

<v-clicks>

Sometimes you have common setup/teardown tasks that you want to perform before/after each test
- You can define a "fixture function" to do the before/after code

```python
import pytest
…

acc = None

@pytest.fixture(autouse=True)
def run_around_tests():
    # Code that will run before each test.
    print("Do something before a test")
    global acc
    acc = BankAccount("David")

    # A test function will be run at this point
    yield

    # Code that will run after each test.
    print("Do something after a test")
```

Note: To see console output with PyTest, use the -s option

</v-clicks>

---

# Using PyHamcrest matchers

- A reminder about simple assertions
- Introducing PyHamcrest
- Getting started with PyHamcrest
- Example class-under-test
- Example test
- Defining a custom PyHamcrest matcher
- Using a custom PyHamcrest matcher

---

# A reminder about simple assertions

<v-clicks>

As we've seen, Python has a simple assert keyword
- assert a == b

What if you want to write some specific tests, such as:
- Does a collection contains a value?
- Does a variable point to a particular type of subclass?
- Does an integer value lie in a certain range?
- Does a double value equal a variable, to a specified accuracy?

</v-clicks>

---

# Introducing PyHamcrest

<v-clicks>

The PyHamcrest library provides a higher-level vocabulary for writing your tests, with "matcher" functions such as:
- equal_to, close_to
- not
- greater_than, greater_than_or_equal_to
- less_than, less_than_or_equal_to
- starts_with, ends_with, contains_string, is_empty
- all_of, any_of
- contains_string, contains_exactly, contains_in_any_order
- has_item, has_items
- has_entry, has_entries, has_key, has_keys, has_value, has_values
- instance_of
- … etc.

</v-clicks>

---

# Getting started with PyHamcrest

Install PyHamcrest as follows:

```
pip install PyHamcrest
```

You can then use PyHamcrest as follows in your tests:

```python
from hamcrest import *
…

assert_that(… … …)
```

---

# Example class-under-test

To illustrate PyHamcrest, we'll test the following class:

```python
class Product:
	
    def __init__(self, description, price, *ratings):
        self.description = description
        self.price = price
        self.ratings = list(ratings)

    def taxPayable(self):
        return self.price * 0.20
    
    def __str__(self):
    	return "{}, £{}, {}".format(self.description, self.price, self.ratings)

```

---

# Example test

```python
from hamcrest import *
import pytest
from Product import Product

product = None

@pytest.fixture(autouse=True)
def run_around_tests():
    global product
    product = Product("TV", 1500, 5, 4, 3, 5, 4, 3)
    yield

def test_product_taxPayable_correct():
    assert_that(product.taxPayable(), close_to(300, 0.1))

def test_product_ratings_containsRating():
    assert_that(product.ratings, has_item(3))

def test_product_ratings_doesntContainsAbsentRating():
    assert_that(product.ratings, not(has_item(2)))
```

---

# Defining a custom PyHamcrest matcher

The PyHamcrest "matcher" model is extensible
- You can define your own custom matcher classes

```python
from hamcrest.core.base_matcher import BaseMatcher


class PriceMatcher(BaseMatcher):

    def __init__(self, maxInclusive=3_000):
        self.maxInclusive = maxInclusive

    def _matches(self, price):
        return 0 < price <= self.maxInclusive

    def describe_to(self, description):
        description.append_text("0..." + str(self.maxInclusive))


def valid_price():
    return PriceMatcher(2_500)
```

---

# Using a custom PyHamcrest matcher

Here's how to use a custom PyHamcrest matcher
- Exactly the same as for the standard PyHamcrest matchers ☺

```python
from hamcrest import *
from priceMatcher import valid_price
from product import Product


def test_product_validPrice_priceAccepted():
    product1 = Product("TV", 1500)
    assert_that(product1.price, valid_price())


def test_product_negativePrice_priceRejected():
    product2 = Product("TV", -1)
    assert_that(product2.price, is_not(valid_price()))


def test_product_tooExpensivePrice_priceRejected():
    product3 = Product("TV", 2501)
    assert_that(product3.price, is_not(valid_price()))
```

---

# Testing techniques

- Parameterized tests
- Running tests selectively
- Grouping tests into sets
- Test Driven Development (TDD)
- Refactoring

---
layout: two-cols
---
# Parameterized tests (1/2)


When you start writing tests, you might notice some of the tests are quite similar and repetitive
- E.g. imagine a function that returns the grade for an exam
- How would you test it always returns the correct grade?

::right::

```python
def get_grade(mark):
    if mark >= 75:
        return "A*"
    elif mark >= 70:
        return "A"
    elif mark >= 60:
        return "B"
    elif mark >= 50:
        return "C"
    elif mark >= 40:
        return "D"
    elif mark >= 30:
        return "E"
    else:
        return "U"
```

---

# Parameterized tests (2/2)

You can write a parameterized test as follows:

```python
import pytest
from util import get_grade

@pytest.mark.parametrize("mark,grade", [
    (99, "A*"),
    (70, "A"),
    (69, "B"),
    (60, "B"),
    (59, "C"),
    (50, "C"),
    (49, "D"),
    (40, "D"),
    (39, "E"),
    (30, "E"),
    (29, "U")])
def test_marks_and_grades(mark, grade):
    assert grade == get_grade(mark)
```

---

# Running tests selectively

test.py lets you specify which test functions to run…

E.g. run all test functions that have 'deposit' in their name
- The -k option specifies the key (function name fragment)
- The -v option displays verbose test results

```bash
py.test -k deposit -v
```

---

# Grouping tests into sets (1/3)

You can group tests into sets
- You can then run all the tests in a particular set

The first step is to specify your custom sets
- Define a file named pytest.ini as follows:

```
[pytest]
markers =
    numtest: mark a test as a numeric test
    strtest: mark a test as a string test
```
> pytest.ini

---

# Grouping tests into sets (2/3)

You can then mark a test function so it belongs to a set(s)
- Decorate the test function with @pytest.mark.aSetName

```python

import pytest

@pytest.mark.numtest
def test_add_numbers():
    assert 3 + 4 == 7

@pytest.mark.numtest
def test_multiple_numbers():
    assert 3 * 4 == 12

@pytest.mark.strtest
def test_concatenate_strings():
    assert "hello " + "world" == "hello world"

@pytest.mark.strtest
def test_uppercase_strings():
    assert "hello world".upper() == "HELLO WORLD"
```

---

# Grouping tests into sets (3/3)

To run all the tests in a particular set:
- Use the -m option 
- Specifies which marked tests to run (i.e. the name of the set)

```
py.test -m numtest -v
```

---

# Test Driven Development (TDD)

<v-clicks>

TDD is a simple concept
- You write the tests first, before your write the code
- The tests act as a specification for the new functionality you're about to implement

In TDD, you perform the following tasks repeatedly:
- Write a test
- Run the test - it must fail!
- Write the minimum amount of code, to make the test pass
- Refactor your code

Benefits of TDD
- Helps you focus on functionality rather than implementation
- Ensures every line of code is tested 

</v-clicks>

---

# Refactoring

<v-clicks>

Refactoring is an oft-overlooked aspect of TDD
- After each iteration through the test-code-pass cycle, you should refactor your code
- That is, step back and see if you can/should reorganize your code to eliminate duplication, restructure inheritance, etc.

Typical refactoring activities:
- Rename a variable / function / class / module
- Extract duplicate code into a common function
- Extract common class functionality into a superclass
- Introduce another level of inheritance

</v-clicks>

---

# Any questions?

---


# GraphCore Requests

---

1. Spawning other processes (subprocess)
2. Regular Expressions
3. Command Line Tools

---

# Spawning Other Processes

- Interacting with the OS
- The subprocess module
- Using subprocess
- Capture the output
- Pass parameters
- Checking the return code
- Running another Python script

---

# Interacting with the OS

There are three key modules that allow us to interact with the host operating system

- The os module enables miscellaneous interfaces with the OS. You can use it to inspect environment variables or to get other user and process-related information. 
- The platform module contains information about the interpreter and the machine where the process is running
- The sys module, which provides you with helpful system-specific information, will usually provide you with all the information that you need about the runtime environment.

---

# The subprocess module

<v-clicks>

- Allows us to start a new process and communicate with it
- This module has gone through some work to modernize and simplify its API and you might see code using subprocess in ways different from those shown here
- There are two main APIs: the `subprocess.run` which is quite high-level and `subprocess.Popen` which is more low level
- We'll focus on the higher level API.
- Dig into the docs if you need more complex interactions

</v-clicks>

---

# Using subprocess

```python
import subprocess
subprocess.run(["ls"])
```

This will run the command in your shell. If you don't have the command you'll raise an exception. 

---

# Capture the output

```python
import subprocess
result = subprocess.run(["ls"], capture_output=True)
print("stdout: ", result.stdout)
print("stderr: ", result.stderr)

```

Adding `text=True` will allow the `stdout` and `stderr` to be strings we can work with.

```python
result = subprocess.run(["ls"], capture_output=True, text=True)
```

---

# Pass Parameters

```python
import subprocess
result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print("stdout: ", result.stdout)
print("stderr: ", result.stderr)
```

Add flags and argumenet in the list. These will be passed through to the shell in the order they are passed.

---

# Checking the return code

```python
result = subprocess.run(["ls", "non_existing_file"])
print("rc: ", result.returncode)
```

You can use the returncode attribute to decide if the process ended without error. 
- 0 is success
- Anything else is some kind of failure

---

# Running another Python script

- You can use `sys.executable` to use the Python executable that is currently running
- We can use this to then run another script

```python
import subprocess
import sys

subprocess.run([sys.executable, "subprocess2.py"])

```

---

# Regular Expressions

- Overview
- Basic Syntax
- Usage

---

# Overview

<v-clicks>

- A domain specific language which defines a grammar for expressing string comparisons
- Easier than having loops of checking for different things
- It's a standard language used across programming languages
- Python's implementation is from the `re` package in the standard library.
- Built into lots of text editors (including PyCharm and VSCode) 

</v-clicks>

---

# Basic Syntax

<v-clicks>

- Most characters match their own identities, so "h" in a regex means "match exactly the letter h."
- Enclosing characters in square brackets can mean choosing between alternates,with "[Hh]" to mean "match either H or h." 
- We use the \S character class to match all non-whitespace. Other character classes include \w (word characters), \W (non-word characters), and \d (digits).
- Two quantifiers are used: 
  - ? means "0 or 1 time,"
  - The quantifier, +, means "1 or more times,"
- Parentheses () introduce a numbered sub-expression, sometimes called a "capture group." 
- A backslash followed by a number refers to a numbered sub-expression, described previously. As an example, \1 refers to the first sub-expression. These can be used when replacing text that matches the regex or to store part of a regex to use later in the same expression. Because of the way that backslashes are interpreted by Python strings, this is written as `\\1` in a Python regex.

</v-clicks>

---

# Usage

```python
import re

title = "And now for something completely different"
pattern = "(\w)\\1+"

print(re.search(pattern, title))
print(re.findall(pattern, title))

reObj = re.compile(pattern)

print(reObj.search(title))
```

---

# Another example

```python
import re

description = "The Norwegian Blue is a wonderful parrot. This parrot is notable for its exquisite plumage."

pattern = "(parrot)"
replacement = "ex-\\1"

print(re.sub(pattern, replacement, description))

```

---

# Command Line Tools

- Parse the arguments
- Carry out some work

---

# Add the parser


There are a number of ways to parse the arguments in Python scripts. A reliable way to do this is with `argparse`.

First, we'll import the library:

```python
import argparse
```

We create a parser object:

```python
# create a parser object
parser = argparse.ArgumentParser(description="A description for our program")
```

---

# Add any arguments

Add any arguments we'd like to:

```python
parser.add_argument("-a", "--add", nargs='*', metavar="num", type=int,
                    help="All the numbers separated by spaces will be added.")

```

<v-clicks>

- The flags that we can pass in (normally single letter with a single dash and full word with a double). The full name will be used to reference the variables
- `nargs` - the number of arguments that come after the flag
- `metavar` - what the variable will be called in the help strings
- `type` - the type of the incoming variables
- `help` - a help string for this argument

</v-clicks>


---

# Parse the arguments and do some work

Once you've add the arguments, we use the parse_args() function.

```python
args = parser.parse_args()
```

Then we can do some work:

```python
if len(args.add) != 0:
    print(sum(args.add))

```
 

---

# Labview links

I don't know enough about Labview to offer insight but here are a few resources I found which might be useful

- https://zone.ni.com/reference/en-XX/help/371361R-01/glang/python_node/
- https://zone.ni.com/reference/en-XX/help/371361R-01/glang/python_pal/
- https://www.youtube.com/watch?v=GApmpZx-Yro
- https://www.youtube.com/watch?v=YL-zGx6u0sQ
- https://github.com/DanielleJobe/LabVIEW2018-Python-Integration-Example/tree/master/py_src

---

# Further Resources

- Mastering Python Regular Expressions book - https://www.packtpub.com/product/mastering-python-regular-expressions/9781783283156

- Automate the Boring Stuff with Python - https://automatetheboringstuff.com/

