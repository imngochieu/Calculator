from tkinter import *

FONT = ("Arial", 9, "bold")

# ------------------ Root ------------------ #
root = Tk()
root.title("Calculator")

# ----------------- Label ------------------ #
result_label = Label(text="0", justify="left", width=37, height=2, bg="light gray")
result_label.grid(column=0, row=0, columnspan=4)

# ----------------- Button ----------------- #
num_1 = Button(text="1", width=8, font=FONT)
num_1.grid(column=0, row=2)

num_2 = Button(text="2", width=8, font=FONT)
num_2.grid(column=1, row=2)

num_3 = Button(text="3", width=8, font=FONT)
num_3.grid(column=2, row=2)

num_4 = Button(text="4", width=8, font=FONT)
num_4.grid(column=0, row=3)

num_5 = Button(text="5", width=8, font=FONT)
num_5.grid(column=1, row=3)

num_6 = Button(text="6", width=8, font=FONT)
num_6.grid(column=2, row=3)

num_7 = Button(text="7", width=8, font=FONT)
num_7.grid(column=0, row=4)

num_8 = Button(text="8", width=8, font=FONT)
num_8.grid(column=1, row=4)

num_9 = Button(text="9", width=8, font=FONT)
num_9.grid(column=2, row=4)

num_0 = Button(text="0", width=18, font=FONT)
num_0.grid(column=0, row=5, columnspan=2)

num_add = Button(text="+", width=8, height=3, font=FONT)
num_add.grid(column=3, row=1, rowspan=2)

num_minus = Button(text="-", width=8, height=3, font=FONT)
num_minus.grid(column=3, row=3, rowspan=2)

num_mul = Button(text="*", width=8, font=FONT)
num_mul.grid(column=1, row=1)

num_div = Button(text="/", width=8, font=FONT)
num_div.grid(column=2, row=1)

num_ac= Button(text="AC", width=8, font=FONT)
num_ac.grid(column=0, row=1)

num_equal = Button(text="=", width=8, font=FONT)
num_equal.grid(column=3, row=5)

num_dot = Button(text=".", width=8, font=FONT)
num_dot.grid(column=2, row=5)




root.mainloop()
