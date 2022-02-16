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

# Bonus

---

- Sharing modules/packages with friends
- Using subprocess

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


# Using subprocess


---

# Further Resources

- Regular Expressions 
    - https://regexcrossword.com/ (practice)
    - https://regexr.com/ (Explainer)

- Books
    - Automate the Boring Stuff with Python