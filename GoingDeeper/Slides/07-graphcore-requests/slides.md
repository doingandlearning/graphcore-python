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
3. LabView

---

# Spawning Other Processes

- Interacting with the OS
- 

---

# Interacting with the OS

There are three key modules that allow us to interact with the host operating system

- The os module enables miscellaneous interfaces with the OS. You can use it to inspect environment variables or to get other user and process-related information. 
- The platform module contains information about the interpreter and the machine where the process is running
- The sys module, which provides you with helpful system-specific information, will usually provide you with all the information that you need about the runtime environment.

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
- Enclosing characters in square brackets can mean choosing between alternates, so if we thought a web link might be capitalized, we could start with "[Hh]" to mean "match either H or h." In the body of the URL, we want to match against any non-whitespace characters, and rather than write them all out. We use
the \S character class. Other character classes include \w (word characters), \W (non-word characters), and \d (digits).
- Two quantifiers are used: ? means "0 or 1 time," so "s?" means "match if the text does not have s at this point or has it exactly once." The quantifier, +, means "1 or more times," so "\S+" says "one or more non-whitespace characters." There is also a quantifier *, meaning "0 or more times."
Additional regex features that you will use in this chapter are listed here:
- Parentheses () introduce a numbered sub-expression, sometimes called a "capture group." They are numbered from 1, in the order that they appear in the expression.
- A backslash followed by a number refers to a numbered sub-expression, described previously. As an example, \1 refers to the first sub-expression. These can be used when replacing text that matches the regex or to store part of a regex to use later in the same expression. Because of the way that backslashes are interpreted by Python strings, this is written as \\1 in a Python regex.

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



# Further Resources

- Mastering Python Regular Expressions book - https://www.packtpub.com/product/mastering-python-regular-expressions/9781783283156