from tkinter import *

root = Tk()
root.title("Calculator")
root.iconbitmap("calculator.ico")
root.geometry("245x243")


global sequence
global outcome
sequence = ""


def add_button(char):
    global sequence
    sequence += char
    sequence.replace("++", "+")
    user_input.delete(0, END)
    user_input.insert(0, sequence)

def equal():
    global sequence
    global outcome
    user_input.delete(0, END)
    if sequence[0].isdigit():
        outcome = eval(sequence)
    else:
        outcome = eval(str(0) + sequence)
    sequence = str(outcome)
    user_input.insert(0, outcome)


def clear_screen():
    global sequence
    sequence = ""
    user_input.delete(0, END)


user_input = Entry(root, font=('Verdana', 14))

button_1 = Button(root, text="1", command=lambda: add_button("1"), padx=25, pady=15)
button_2 = Button(root, text="2", command=lambda: add_button("2"), padx=25, pady=15)
button_3 = Button(root, text="3", command=lambda: add_button("3"), padx=25, pady=15)
button_4 = Button(root, text="4", command=lambda: add_button("4"), padx=25, pady=15)
button_5 = Button(root, text="5", command=lambda: add_button("5"), padx=25, pady=15)
button_6 = Button(root, text="6", command=lambda: add_button("6"), padx=25, pady=15)
button_7 = Button(root, text="7", command=lambda: add_button("7"), padx=25, pady=15)
button_8 = Button(root, text="8", command=lambda: add_button("8"), padx=25, pady=15)
button_9 = Button(root, text="9", command=lambda: add_button("9"), padx=25, pady=15)
button_0 = Button(root, text="0", command=lambda: add_button("0"), padx=25, pady=15)

button_plus = Button(root, text="+", command=lambda: add_button("+"), padx=16.5, pady=15)
button_minus = Button(root, text="-", command=lambda: add_button("-"), padx=18, pady=15)
button_multiply = Button(root, text="*", command=lambda: add_button("*"), padx=18, pady=15)
button_divide = Button(root, text="/", command=lambda: add_button("/"), padx=18, pady=15)
button_equal_to = Button(root, text="=", command=equal, padx=24, pady=15)
button_clear = Button(root, text="Clear", command=clear_screen, padx=15, pady=15)


user_input.grid(column=0, row=0, columnspan=4)

button_1.grid(column=0, row=3)
button_2.grid(column=1, row=3)
button_3.grid(column=2, row=3)
button_4.grid(column=0, row=2)
button_5.grid(column=1, row=2)
button_6.grid(column=2, row=2)
button_7.grid(column=0, row=1)
button_8.grid(column=1, row=1)
button_9.grid(column=2, row=1)
button_0.grid(column=1, row=4)

button_plus.grid(column=3, row=1)
button_minus.grid(column=3, row=2)
button_multiply.grid(column=3, row=3)
button_divide.grid(column=3, row=4)
button_equal_to.grid(column=2, row=4)
button_clear.grid(column=0, row=4)

mainloop()
