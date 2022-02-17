import tkinter as tk
from random import randint

window = tk.Tk()

count = 0


def increase():
    global count
    count += 1
    greeting["text"] = f"You've clicked the button {count} times"


def roll():
    diceLabel["text"] = f"{randint(1, 6)}"


greeting = tk.Label(text="Hello, GraphCore", foreground="white", background="black")
greeting.pack()

button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    master=window,
    command=increase
)

diceButton = tk.Button(
    text="Click to roll a 6 sided dice",
    width=25,
    height=5,
    master=window,
    command=roll
)

button.pack()
diceButton.pack()

diceLabel = tk.Label(text="You haven't rolled yet, click above.")

diceLabel.pack()

entryLabel = tk.Label(text="Enter a temperature in F and click the button below")


def convert():
    f_temp = entry.get()
    c_temp = (5 / 9) * (float(f_temp) - 32)
    tempResult["text"] = f"{f_temp} degrees F is {c_temp} degrees C."


entry = tk.Entry(fg="yellow", bg="blue", width=50)
entryButton = tk.Button(
    text="Convert",
    master=window,
    command=convert
)
tempResult = tk.Label()

entryLabel.pack()
entry.pack()
entryButton.pack()
tempResult.pack()

window.mainloop()
