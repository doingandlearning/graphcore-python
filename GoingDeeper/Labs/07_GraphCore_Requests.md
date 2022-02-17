# GraphCore Requests

# Overview

This is an opportunity to practice with some of the specific techniques and features that were requested during the
first days of the course.

If there are more you'd like to explore on Day 4 let me know.

We'll cover using the subprocess module and regular expressions.

# Roadmap

1. Testing Python Code by spawning other processes
2. Regular expression practice
3. Command Line Tool

# Exercise 1: Testing Python Code by spawning other processes

A company that receives small Python code snippets from its clients with basic mathematical and string operations has
realized that some of the operations crash their platform. There is some asked for code requested by clients that cause
the Python interpreter to abort as it cannot compute it.

This is an example:

compile("1" + "+1" * 10 ** 6, "string", "exec")

You are therefore asked to create a small program that can run the requested code and check whether it will crash
without breaking the current process. This can be done by running the same code with subprocess and the same interpreter
version that is currently running the code.

To get this code, you need to:

1. Find out the executable of our interpreter by using the sys module.

2. Use subprocess to run the code with the interpreter that you used in the previous step.

3. Use the -c option of the interpreter to run code inline.

4. Check whether the result code is -11, which corresponds to an abort in the program.

# Exercise 2: Regular Expression Practice

At your online retail company, your manager has had an idea for a promotion. There is a whole load of old "The X-Files"
DVDs in the warehouse, and she has decided to give one away for free to any customer whose name contains the letter x.

In this lab, you will be using Python's re module to find winning customers. The x could be capitalized if it's their
initial, or lower case if it's in the middle of their name, so use the regular expression [Xx] to search for both cases:

1. Create a list of customer names. The customers are Xander Harris, Jennifer Smith, Timothy Jones, Amy Alexandrescu,
   Peter Price, and Weifung Xu.

2. Create a list comprehension using the list of names. Use the comprehension to filter only names where a search for
   the [Xx] regex is successful.

3. Print the list of matching names. The result should look like this:

       ['Xander Harris', 'Amy Alexandrescu', 'Weifung Xu']

# Exercise 3: Command Line Tool

Run `exercise3.py` from the command line with some arguments to check it can work.

```bash
python exercise3.py --add 1 2 3
```

Extend the program to allow you to multiply the parameters with a different flag.

Hints:

- The new argument could have both types of flag
- One way to multiply a list of numbers is to use the reduce function

```python
from functools import reduce

# this is if your argument was called multiply.
if args.multiply and len(args.multiply) != 0:
    print(reduce(lambda x, y: x * y, args.multiply))

```