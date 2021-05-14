# Calculator


from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# defining window
win = Tk()
win.title("Calculator")
win.resizable(False, False)
win.config(bg="white")

my_calc = ttk.Notebook(win)
my_calc.grid()

frame1 = Frame(my_calc)
frame2 = Frame(my_calc, bg="#9eb5d9")
frame1.grid()
frame2.grid()

my_calc.add(frame1, text="Calculator")
my_calc.add(frame2, text="Converter")

show_btn = Entry(frame1, justify=RIGHT, font=("arial", 15, "bold"),
                 width=26, relief="solid", bg="#6a6e6b", borderwidth=6)
show_btn.grid(row=0, column=0, columnspan=5, padx=10, pady=10)


def btn_click(num):
    x = show_btn.get()
    show_btn.delete(0, END)
    show_btn.insert(0, str(x) + str(num))


def btn_add():
    first_num = show_btn.get()
    global f_num
    global math
    math = "addition"
    try:
        f_num = int(first_num)
        show_btn.delete(0, END)
    except ValueError:
        pass


def btn_sub():
    first_num = show_btn.get()
    global f_num
    global math
    math = "subtraction"
    try:
        f_num = int(first_num)
        show_btn.delete(0, END)
    except ValueError:
        pass


def btn_mul():
    first_num = show_btn.get()
    global f_num
    global math
    math = "multiplication"
    try:
        f_num = int(first_num)
        show_btn.delete(0, END)
    except ValueError:
        pass


def btn_div():
    first_num = show_btn.get()
    global f_num
    global math
    math = "division"
    try:
        f_num = int(first_num)
        show_btn.delete(0, END)
    except ValueError:
        pass


def btn_equal():
    try:
        second_num = show_btn.get()
        show_btn.delete(0, END)
        if math == "addition":
            show_btn.insert(0, f_num + int(second_num))
        elif math == "subtraction":
            show_btn.insert(0, f_num - int(second_num))
        elif math == "multiplication":
            show_btn.insert(0, f_num * int(second_num))
        elif math == "division":
            show_btn.insert(0, f_num // int(second_num))
    except NameError or ValueError:
        pass


def btn_clear():
    show_btn.delete(0, END)


# Creating Number Buttons


btn_1 = Button(frame1, text="1",
               padx=15, pady=2, relief="solid",
               font=("Verdana", 15), borderwidth=3,
               activeforeground="#5e0808", command=lambda: btn_click(1))
btn_2 = Button(frame1, text="2",
               padx=15, pady=2, relief="solid",
               font=("Verdana", 15), borderwidth=3,
               activeforeground="#5e0808", command=lambda: btn_click(2))
btn_3 = Button(frame1, text="3",
               padx=15, pady=2, relief="solid",
               font=("Verdana", 15), borderwidth=3,
               activeforeground="#5e0808", command=lambda: btn_click(3))
btn_4 = Button(frame1, text="4",
               padx=15, pady=2, relief="solid",
               font=("Verdana", 15), borderwidth=3,
               activeforeground="#5e0808", command=lambda: btn_click(4))
btn_5 = Button(frame1, text="5",
               padx=15, pady=2, relief="solid",
               font=("Verdana", 15), borderwidth=3,
               activeforeground="#5e0808", command=lambda: btn_click(5))
btn_6 = Button(frame1, text="6",
               padx=15, pady=2, relief="solid",
               font=("Verdana", 15), borderwidth=3,
               activeforeground="#5e0808", command=lambda: btn_click(6))
btn_7 = Button(frame1, text="7",
               padx=15, pady=2, relief="solid",
               font=("Verdana", 15), borderwidth=3,
               activeforeground="#5e0808", command=lambda: btn_click(7))
btn_8 = Button(frame1, text="8",
               padx=15, pady=2, relief="solid",
               font=("Verdana", 15), borderwidth=3,
               activeforeground="#5e0808", command=lambda: btn_click(8))
btn_9 = Button(frame1, text="9",
               padx=15, pady=2, relief="solid",
               font=("Verdana", 15), borderwidth=3,
               activeforeground="#5e0808", command=lambda: btn_click(9))
btn_0 = Button(frame1, text="0",
               padx=15, pady=2, relief="solid",
               font=("Verdana", 15), borderwidth=3,
               activeforeground="#5e0808", command=lambda: btn_click(0))

# Creating Operation Buttons


btn_add = Button(frame1, text="+", bg="#857b7b",
                 padx=51, pady=2, relief="solid",
                 font=("Verdana", 15), borderwidth=3,
                 activeforeground="#5e0808", command=btn_add)
btn_sub = Button(frame1, text="-", bg="#857b7b",
                 padx=55, pady=2, relief="solid",
                 font=("Verdana", 15), borderwidth=3,
                 activeforeground="#5e0808", command=btn_sub)
btn_mul = Button(frame1, text="x", bg="#857b7b",
                 padx=53, pady=2, relief="solid", font=("Verdana", 15),
                 borderwidth=3, activeforeground="#5e0808", command=btn_mul)
btn_div = Button(frame1, text="÷", bg="#857b7b",
                 padx=51, pady=2, relief="solid", font=("Verdana", 15),
                 borderwidth=3, activeforeground="#5e0808", command=btn_div)

btn_equal = Button(frame1, text="=",
                   padx=14, pady=2, relief="solid", font=("Verdana", 15),
                   borderwidth=3, activeforeground="#5e0808",
                   command=btn_equal)
btn_clear = Button(frame1, text="C",
                   padx=14, pady=2, relief="solid", font=("Verdana", 15),
                   borderwidth=3, activeforeground="#5e0808",
                   command=btn_clear)

# # Lay out widgets


btn_1.grid(row=3, column=0)
btn_2.grid(row=3, column=1)
btn_3.grid(row=3, column=2)
btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)
btn_7.grid(row=1, column=0)
btn_8.grid(row=1, column=1)
btn_9.grid(row=1, column=2)
btn_0.grid(row=4, column=0)

btn_add.grid(row=1, column=3)
btn_sub.place(x=188, y=106)
btn_mul.grid(row=3, column=3)
btn_div.grid(row=4, column=3)

btn_equal.place(x=125, y=202)
btn_clear.grid(row=4, column=1)


###############################################################################


# Converter, BMI


def get_height():
    height = float(ENTRY2.get())
    return height


def get_weight():
    weight = float(ENTRY1.get())
    return weight


def calculate_bmi(a=""):
    print(a)

    try:
        height = get_height()
        weight = get_weight()
        height = height / 100.0
        bmi = weight / (height ** 2)
    except ZeroDivisionError:
        messagebox.showinfo("Result", "Please enter positive height!!")
    except ValueError:
        messagebox.showinfo("Result", "Please enter valid data!")
    else:
        if bmi <= 15.0:
            res = "Your BMI is " + str(bmi) + \
                  "\nRemarks: Very severely underweight!!"
            messagebox.showinfo("Result", res)
        elif 15.0 < bmi <= 16.0:
            res = "Your BMI is " + str(bmi) + \
                  "\nRemarks: Severely underweight!"
            messagebox.showinfo("Result", res)
        elif 16.0 < bmi < 18.5:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Underweight!"
            messagebox.showinfo("Result", res)
        elif 18.5 <= bmi <= 25.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Normal."
            messagebox.showinfo("Result", res)
        elif 25.0 < bmi <= 30:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Overweight."
            messagebox.showinfo("Result", res)
        elif 30.0 < bmi <= 35.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Moderately obese!"
            messagebox.showinfo("Result", res)
        elif 35.0 < bmi <= 40.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Severely obese!"
            messagebox.showinfo("Result", res)
        else:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Super obese!!"
            messagebox.showinfo("Result", res)


LABLE = Label(frame2, bg="#307678", text="Welcome to BMI Calculator",
              font=("Helvetica", 10, "bold"), pady=10)
LABLE.place(x=0, y=120)
LABLE1 = Label(frame2, bg="#cef0f1", text="Enter Weight (in kg):", bd=6,
               font=("Helvetica", 8, "bold"), pady=5)
LABLE1.place(x=55, y=160)
ENTRY1 = Entry(frame2, bd=1, width=6, font="Roboto 11")
ENTRY1.place(x=200, y=170)
LABLE2 = Label(frame2, bg="#cef0f1", text="Enter Height (in cm):", bd=6,
               font=("Helvetica", 8, "bold"), pady=5)
LABLE2.place(x=55, y=190)
ENTRY2 = Entry(frame2, bd=1, width=6, font="Roboto 11")
ENTRY2.place(x=200, y=200)
BUTTON = Button(frame2, bg="#2187e7", bd=8, relief="solid",
                text="BMI", padx=0, pady=5, command=calculate_bmi,
                font=("Helvetica", 10, "bold"))

BUTTON.place(x=275, y=172)
LABLE3 = Label(frame2, bg="#9eb5d9",
               text="_______________________________________________________",
               bd=6, font=("Helvetica", 8, "bold"))
LABLE3.place(x=-7, y=100)


###############################################################################


def convert_fahr():
    try:
        words = fbtext.get()
        ftemp = float(words)
        celbox.delete(0, END)
        celbox.insert(0, '%.2f' % (tocel(ftemp)))
        kelbox.delete(0, END)
        kelbox.insert(0, '%.2f' % (tokel(tocel(ftemp))))
        return
    except ValueError:
        pass


def convert_cel():
    try:
        words = cbtext.get()
        ctemp = float(words)
        fahrbox.delete(0, END)
        fahrbox.insert(0, '%.2f' % (tofahr(ctemp)))
        kelbox.delete(0, END)
        kelbox.insert(0, '%.2f' % (tokel(ctemp)))
    except ValueError:
        pass


def convert_kel():
    try:
        words = kbtext.get()
        ktemp = float(words)
        fahrbox.delete(0, END)
        fahrbox.insert(0, '%.2f' % (tofahr(ktoc(ktemp))))
        celbox.delete(0, END)
        celbox.insert(0, '%.2f' % (ktoc(ktemp)))
    except ValueError:
        pass


def tocel(fahr):
    return (fahr - 32) * 5.0 / 9.0


def tofahr(cel):
    return cel * 9.0 / 5.0 + 32


def ktoc(kel):
    return kel - 273.15


def tokel(cel):
    return cel + 273.15


fahrlabel = Label(frame2, bg="#cef0f1", text='Fahrenheit')
fahrlabel.grid(row=0, column=0, padx=5, pady=5, sticky=E)

cellabel = Label(frame2, bg="#cef0f1", text='Celsius')
cellabel.grid(row=1, column=0, padx=5, pady=5, sticky=E)

kellabel = Label(frame2, bg="#cef0f1", text='Kelvin')
kellabel.grid(row=2, column=0, padx=5, pady=5, sticky=E)

fbtext = StringVar()
fbtext.set('')
fahrbox = Entry(frame2, textvariable=fbtext)
fahrbox.grid(row=0, column=1)

cbtext = StringVar()
cbtext.set('')
celbox = Entry(frame2, textvariable=cbtext)
celbox.grid(row=1, column=1)

kbtext = StringVar()
kbtext.set('')
kelbox = Entry(frame2, textvariable=kbtext)
kelbox.grid(row=2, column=1)

fgobutton = Button(frame2, text='Go', bg="#2187e7", command=convert_fahr)
fgobutton.grid(row=0, column=2, padx=5, pady=5, sticky=N + S + E + W)

cgobutton = Button(frame2, text='Go', bg="#2187e7", command=convert_cel)
cgobutton.grid(row=1, column=2, padx=5, pady=5, sticky=N + S + E + W)

kgobutton = Button(frame2, text='Go', bg="#2187e7", command=convert_kel)
kgobutton.grid(row=2, column=2, padx=5, pady=5, sticky=N + S + E + W)

win.mainloop()
