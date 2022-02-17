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

